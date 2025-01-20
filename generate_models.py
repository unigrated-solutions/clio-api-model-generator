import os
import json
import requests
import shutil
from pathlib import Path

# Path to the OpenAPI spec file
SPEC_FILE_URL = 'https://docs.developers.clio.com/openapi.json'
SPEC_FILE_PATH = 'openapi.json'
STATIC_DIR = 'static'
MODELS_DIR = 'models'

def init_models():
    def find_and_backup_models_folder():
        """Check if 'models' exists in the parent directory first, then in the project root, and handle backup."""
        current_dir = Path(os.getcwd())
        parent_dir = current_dir.parent

        # Check the parent directory first as the preferred location
        for directory in [parent_dir, current_dir]:
            models_path = directory / MODELS_DIR

            if models_path.exists():
                if any(models_path.iterdir()):  # If the directory is not empty
                    print(f'Existing non-empty models directory found at: {models_path}')
                    backup_folder = models_path.with_name(f"{MODELS_DIR}.backup")
                    counter = 1

                    # Find a unique backup folder name
                    while backup_folder.exists():
                        backup_folder = models_path.with_name(f"{MODELS_DIR}.backup{counter}")
                        counter += 1
                    
                    os.rename(models_path, backup_folder)
                    print(f'Renamed "{models_path}" to "{backup_folder}"')

                    # Create a new models directory in the same location
                    models_path.mkdir(parents=True, exist_ok=True)
                    print(f'Created new "{models_path}" directory.')

                    return models_path  # Return the parent models directory
                else:
                    print(f'Models folder found at "{models_path}" but it is empty.')
                    return models_path  # Return the empty parent models directory

        print(f'No existing "{MODELS_DIR}" directory found in parent or current directory.')
        return None

    def backup_and_create_models_folder():
        """Handles model folder backup and creation in the parent directory as default, else locally."""
        models_path = find_and_backup_models_folder() or Path(MODELS_DIR).resolve()

        if not models_path.exists():
            models_path.mkdir(parents=True, exist_ok=True)
            print(f'Created new "{models_path}" directory.')

        # Copy all files from 'static/' to the determined models folder
        if Path(STATIC_DIR).exists():
            for item in Path(STATIC_DIR).iterdir():
                if item.is_file():
                    shutil.copy2(item, models_path / item.name)
            print(f'Copied all files from "{STATIC_DIR}" to "{models_path}".')
        else:
            print(f'Static directory "{STATIC_DIR}" not found, no files copied.')

        # Set the models directory in environment variables for the generator scripts
        os.environ["ENDPOINTS_PATH"] = str(models_path / "endpoints.py")
        os.environ["FIELDS_PATH"] = str(models_path / "fields.py")
        os.environ["QUERY_PATH"] = str(models_path / "query.py")
        os.environ["REQUEST_BODY_PATH"] = str(models_path / "request_body.py")
        os.environ["SCHEMA_PATH"] = str(models_path / "schemas.py")

        print(f'Set environment variables for model paths: {models_path}')

    def download_api_specs():
        """Downloads OpenAPI specifications if the file does not already exist."""
        if not Path(SPEC_FILE_PATH).exists():
            try:
                response = requests.get(SPEC_FILE_URL)
                if response.status_code == 200:
                    with open(SPEC_FILE_PATH, 'wb') as file:
                        file.write(response.content)
                    print('File downloaded successfully')
                    os.environ["SPEC_FILE_PATH"] = str(SPEC_FILE_PATH)
                else:
                    print('Failed to download file')
            except requests.RequestException as e:
                print(f'Error downloading file: {e}')
        else:
            print("API specs found")
            os.environ["SPEC_FILE_PATH"] = str(SPEC_FILE_PATH)
            
    backup_and_create_models_folder()
    download_api_specs()
    
init_models()

from generators.schema import generate_schema_dataclasses
from generators.fields import generate_field_dataclasses
from generators.query import generate_query_dataclass
from generators.request_body import generate_request_body_dataclass
from generators.endpoints import generate_endpoint_registry  

def generate_models():
    with open(SPEC_FILE_PATH, "r") as f:
        json_spec = json.load(f)

    paths = json_spec.get("paths", {})
    endpoint_definitions = []

    generate_schema_dataclasses()
    field_mapping = generate_field_dataclasses()
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

    print(f'Dataclasses generated in {Path(os.getenv("QUERY_PATH", "models/query.py"))}')
    print(f'Dataclasses generated in {Path(os.getenv("REQUEST_BODY_PATH", "models/request_body.py"))}')
    
if __name__ == "__main__":

    generate_models()
