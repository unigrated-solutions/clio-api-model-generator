import os
import sys
import json
import requests
import shutil
from pathlib import Path
import yaml

from .config import *
print("Generating from:", SPEC_FILE_URL)

from .components import generate_component_dataclasses
from .fields import generate_field_dataclasses
from .query import generate_query_dataclass
from .request_body import generate_request_body_dataclass
from .endpoints import generate_endpoint_registry


def download_api_specs(dest_path=DOWNLOADED_SPEC_PATH) -> Path | None:
    try:
        response = requests.get(SPEC_FILE_URL)
        if response.status_code == 200:
            with open(dest_path, 'wb') as file:
                file.write(response.content)
            print(f'✅ OpenAPI spec downloaded to: {dest_path}')
            return dest_path
        else:
            print(f'❌ Failed to download spec file, status: {response.status_code}')
            return None
    except requests.RequestException as e:
        print(f'❌ Error downloading file: {e}')
        return None
        
def load_openapi_spec(file_path=None):
    """Loads an OpenAPI spec file (JSON or YAML) and returns it as a Python dictionary."""

    if file_path is None:
        file_path = download_api_specs()
        if file_path is None:
            raise RuntimeError("Failed to download OpenAPI spec.")

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"Spec file does not exist: {file_path}")

    with open(file_path, "r", encoding="utf-8") as file:
        if file_path.suffix == ".json":
            return json.load(file)
        elif file_path.suffix in (".yaml", ".yml"):
            return yaml.safe_load(file)
        else:
            raise ValueError(f"Unsupported file extension: {file_path.suffix}")

def generate_models(file_path=None, output_dir=SCRIPT_DIR, **kwargs):
    """
    Generate all dataclass models from the OpenAPI spec.
    If no file_path is provided, the latest spec will be downloaded.
    """
    openapi_spec = load_openapi_spec(file_path)

    paths = openapi_spec.get("paths", {})
    endpoint_definitions = []

    generate_component_dataclasses(openapi_spec)
    field_mapping = generate_field_dataclasses(openapi_spec)
    # print(field_mapping)
    for path, methods in paths.items():
        for method, details in methods.items():
            # Format the class name
            class_name = details["operationId"].replace("#", "_").replace(".", "_").capitalize()

            # Generate query dataclass
            parameters = details.get("parameters", [])
            responses = details.get("responses", {})
            
            field_model = None
            field = responses.get("200",{}).get("content",{}).get("application/json; charset=utf-8",{}).get("schema",{}).get("$ref")
            if not field:
                field = responses.get("201",{}).get("content",{}).get("application/json; charset=utf-8",{}).get("schema",{}).get("$ref")
            if field:
                list_show_mapping_key = field.split("/")[-1]
                field_model = field_mapping.get(list_show_mapping_key)
                
            query_model_name = f"{class_name}_Query"
            if parameters:
                generate_query_dataclass(query_model_name, parameters)

            # Prepare endpoint metadata for registry
            endpoint = {
                "name": class_name,
                "path": path,
                "method": method.upper(),
                "query_model": query_model_name if parameters else None,
                "request_body_model": None,
                "field_model": field_model
            }

            # Generate request body dataclass if present
            if "requestBody" in details:
                request_body_model_name = f"{class_name}_RequestBody"
                generate_request_body_dataclass(request_body_model_name, details["requestBody"])
                endpoint["request_body_model"] = request_body_model_name

            # Append to endpoint definitions
            endpoint_definitions.append(endpoint)

    # Generate endpoints dynamically in the registry
    generate_endpoint_registry(endpoint_definitions)
    export_temp_contents(target_path=output_dir, **kwargs)
    
def update():
    download_api_specs()
    generate_models()

# def init_models():
#     def find_and_backup_models_folder():
#         """Check if 'models' exists in the current directory and handle backup."""
#         models_path = Path(MODELS_DIR).resolve()

#         if models_path.exists():
#             if any(models_path.iterdir()):  # If the directory is not empty
#                 print(f'Existing non-empty models directory found at: {models_path}')
#                 backup_folder = models_path.with_name(f"{MODELS_DIR}.backup")
#                 counter = 1

#                 # Find a unique backup folder name
#                 while backup_folder.exists():
#                     backup_folder = models_path.with_name(f"{MODELS_DIR}.backup{counter}")
#                     counter += 1
                
#                 os.rename(models_path, backup_folder)
#                 print(f'Renamed "{models_path}" to "{backup_folder}"')

#                 # Create a new models directory
#                 models_path.mkdir(parents=True, exist_ok=True)
#                 print(f'Created new "{models_path}" directory.')

#                 return models_path  # Return the models directory
#             else:
#                 print(f'Models folder found at "{models_path}" but it is empty.')
#                 return models_path  # Return the empty models directory

#         print(f'No existing "{MODELS_DIR}" directory found, creating a new one.')
#         return None

#     def backup_and_create_models_folder():
#         """Handles model folder backup and creation."""
#         models_path = find_and_backup_models_folder() or Path(MODELS_DIR).resolve()

#         if not models_path.exists():
#             models_path.mkdir(parents=True, exist_ok=True)
#             print(f'Created new "{models_path}" directory.')

#         # Copy all files from the static directory to the models folder
#         static_path = Path(LOCAL_STATIC_DIR)
#         if static_path.exists():
#             for item in static_path.iterdir():
#                 if item.is_file():
#                     shutil.copy2(item, models_path / item.name)
#             print(f'Copied all files from "{LOCAL_STATIC_DIR}" to "{models_path}".')
#         else:
#             print(f'Static directory "{LOCAL_STATIC_DIR}" not found, no files copied.')

#         # Set the models directory and spec file path in environment variables
#         os.environ["SPEC_FILE_PATH"] = str(Path(SPEC_FILE_PATH).resolve())
#         os.environ["ENDPOINTS_PATH"] = str(models_path / "endpoints.py")
#         os.environ["FIELDS_PATH"] = str(models_path / "fields.py")
#         os.environ["QUERY_PATH"] = str(models_path / "query.py")
#         os.environ["REQUEST_BODY_PATH"] = str(models_path / "request_body.py")
#         os.environ["COMPONENT_PATH"] = str(models_path / "components.py")

#         print(f'Set environment variables for model paths: {models_path}')
#         print(f'Set environment variable SPEC_FILE_PATH: {os.environ["SPEC_FILE_PATH"]}')

#     backup_and_create_models_folder()
    
# init_models()

# def main():
#     if len(sys.argv) > 1 and sys.argv[1] == "update":
#         update()
#     else:
#         generate_models()

# if __name__ == "__main__":
#     main()