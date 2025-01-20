# Model Generator Setup Guide

**This document explains the setup process for handling the `models` directory, running generator scripts, and ensuring the correct paths are set dynamically.**

**TODO: Update README to explain how the model dataclasses are generated from API Specs**

## Overview

The project handles the `models` directory in the following way:

1. **Checks for the existence of the `models` folder in the parent directory first (preferred).**
2. **If not found in the parent, it checks the project root directory.**
3. **If the folder exists and is not empty, it is backed up with a unique name (e.g., `models.backup`, `models.backup1`, etc.).**
4. **If no models folder is found, a new one is created in the preferred location (parent or project root).**
5. **Static files from the `static/` directory are copied into the models folder.**
6. **Environment variables are set to ensure the generator scripts use the correct folder paths.**
7. **Generator scripts are imported after paths are set.**

## Setup Process

### 1. Backup and Creation of `models` Folder

The following logic is used to determine where the `models` directory should be:

```python
from pathlib import Path
import os
import shutil

MODELS_DIR = 'models'
STATIC_DIR = 'static'

def find_and_backup_models_folder():
    current_dir = Path(os.getcwd())
    parent_dir = current_dir.parent

    for directory in [parent_dir, current_dir]:
        models_path = directory / MODELS_DIR

        if models_path.exists():
            if any(models_path.iterdir()):
                print(f'Existing non-empty models directory found at: {models_path}')
                backup_folder = models_path.with_name(f"{MODELS_DIR}.backup")
                counter = 1

                while backup_folder.exists():
                    backup_folder = models_path.with_name(f"{MODELS_DIR}.backup{counter}")
                    counter += 1

                os.rename(models_path, backup_folder)
                print(f'Renamed "{models_path}" to "{backup_folder}"')

                models_path.mkdir(parents=True, exist_ok=True)
                print(f'Created new "{models_path}" directory.')
                return models_path

            else:
                print(f'Models folder found at "{models_path}" but it is empty.')
                return models_path

    print(f'No existing "{MODELS_DIR}" directory found in parent or current directory.')
    return None
```

### 2. Copying Static Files

Once the `models` folder is created or selected, the files from `static/` are copied:

```python
def backup_and_create_models_folder():
    models_path = find_and_backup_models_folder() or Path(MODELS_DIR).resolve()

    if not models_path.exists():
        models_path.mkdir(parents=True, exist_ok=True)
        print(f'Created new "{models_path}" directory.')

    if Path(STATIC_DIR).exists():
        for item in Path(STATIC_DIR).iterdir():
            if item.is_file():
                shutil.copy2(item, models_path / item.name)
        print(f'Copied all files from "{STATIC_DIR}" to "{models_path}".')
    else:
        print(f'Static directory "{STATIC_DIR}" not found, no files copied.')

    os.environ["ENDPOINTS_PATH"] = str(models_path / "endpoints.py")
    os.environ["FIELDS_PATH"] = str(models_path / "fields.py")
    os.environ["QUERY_PATH"] = str(models_path / "query.py")
    os.environ["REQUEST_BODY_PATH"] = str(models_path / "request_body.py")
    os.environ["SCHEMA_PATH"] = str(models_path / "schemas.py")

    print(f'Set environment variables for model paths: {models_path}')
```

### 3. Running the Setup and Importing Generators

The functions are executed in the following order:

```python
if __name__ == "__main__":
    backup_and_create_models_folder()

    from generators.schema import generate_schema_dataclasses
    from generators.fields import generate_field_dataclasses
    from generators.query import generate_query_dataclass
    from generators.request_body import generate_request_body_dataclass
    from generators.endpoints import generate_endpoint_registry  

    print("All setup and generator scripts loaded successfully.")
```

### 4. Generator Scripts

The generator scripts should use the environment variables to reference paths dynamically:

```python
import os
from pathlib import Path

ENDPOINTS_PATH = Path(os.getenv("ENDPOINTS_PATH", "models/endpoints.py"))
FIELDS_PATH = Path(os.getenv("FIELDS_PATH", "models/fields.py"))
QUERY_PATH = Path(os.getenv("QUERY_PATH", "models/query.py"))
REQUEST_BODY_PATH = Path(os.getenv("REQUEST_BODY_PATH", "models/request_body.py"))
SCHEMA_PATH = Path(os.getenv("SCHEMA_PATH", "models/schemas.py"))

print(f"Using ENDPOINTS_PATH: {ENDPOINTS_PATH}")
print(f"Using FIELDS_PATH: {FIELDS_PATH}")
```

## Execution Flow Summary

1. **Check parent directory for `models` folder first.**  
2. **Backup existing folder if not empty and create a new one.**  
3. **Copy static files into the models folder.**  
4. **Set environment variables with the correct paths.**  
5. **Import generator scripts that rely on the updated paths.**  

## Expected Outputs

### Case 1: Models folder found in the parent directory and backed up
```
Existing non-empty models directory found at: /home/user/models
Renamed "/home/user/models" to "/home/user/models.backup"
Created new "/home/user/models" directory.
Copied all files from "static/" to "/home/user/models".
Set environment variables for model paths: /home/user/models
```

### Case 2: No models folder found, creating a new one
```
No existing "models" directory found in parent or current directory.
Created new "/home/user/project/models" directory.
Copied all files from "static/" to "/home/user/project/models".
Set environment variables for model paths: /home/user/project/models
```

---

## Notes

- Ensure the `static/` directory exists and contains the required files before running the script.
- The parent directory is prioritized when determining the location of the `models` folder.
- Environment variables are crucial to dynamically set paths without modifying scripts manually.

