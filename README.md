## Update 3/21/25: Added models generated for Clio Grow API for testing purposes
 - **We don't have much experience with how Clio Grow is being used**
 - **This model generator is structured so that it can be used with any platform with an API following OpenAPI standards**
 - **Feel free to reach out if you have any questions or have other platforms that you might want to fine tune this generator/api client for!**

# Model Generator Setup Guide

**This document explains the setup process for handling the `models` directory, running generator scripts, and ensuring the correct paths are set dynamically.**

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

### 3. Generator Scripts

The generator scripts should use the environment variables to reference paths dynamically:

```python
ENDPOINTS_PATH = Path(os.getenv("ENDPOINTS_PATH", "models/endpoints.py"))
FIELDS_PATH = Path(os.getenv("FIELDS_PATH", "models/fields.py"))
QUERY_PATH = Path(os.getenv("QUERY_PATH", "models/query.py"))
REQUEST_BODY_PATH = Path(os.getenv("REQUEST_BODY_PATH", "models/request_body.py"))
SCHEMA_PATH = Path(os.getenv("SCHEMA_PATH", "models/schemas.py"))
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

---

# Dataclass Generator Scripts

This document provides an overview of the dataclass generator scripts, explaining their order of execution, flow, and parsing/extraction logic for each generator.

## Overview

The scripts process an OpenAPI specification to generate Python dataclasses for:

1. **Schemas** – Representing API response objects.
2. **Fields** – Handling OpenAPI field mappings.
3. **Query Parameters** – Handling API query parameters.
4. **Request Bodies** – Handling request payloads.
5. **Endpoints** – Registering API endpoints with generated models.

---

## Order of Execution

The generation process is orchestrated by `generate_models.py`, which follows this sequence:

1. **Initialization (folder setup and OpenAPI spec download)**
   - Ensures the `models` directory is ready.
   - Downloads the OpenAPI spec if not present.

2. **Schema Generation (`schema.py`)**
   - Generates dataclasses from OpenAPI schemas.

3. **Field Extraction (`fields.py`)**
   - Extracts field definitions for models based on schema dependencies.

4. **Query Parameter Handling (`query.py`)**
   - Creates query dataclasses based on API query parameters.

5. **Request Body Handling (`request_body.py`)**
   - Processes and generates dataclasses for API request bodies.

6. **Endpoint Registry Creation (`endpoints.py`)**
   - Registers generated models to the API endpoint paths.

---

## Parsing and Extraction Logic

### 1. **Schema Generator (`schema.py`)**

**Purpose:**  
Processes OpenAPI `components.schemas` to generate Python dataclasses.

**Key Logic:**  
- Reads the OpenAPI spec from `SPEC_FILE_PATH`.
- Iterates over schemas containing `_base` in the name.
- Recursively processes properties:
  - Required fields are listed first.
  - Optional fields are annotated with `Optional`.
- Handles nested objects by generating sub-dataclasses.

**Example Output:**

```python
@dataclass
class UserBase:
    id: int
    name: str
    email: Optional[str] = None
```

---

## Fields Generation (`fields.py`)

### **Purpose**

The `fields.py` script generates dataclasses that represent OpenAPI schema field definitions, including handling dependencies and nested resources.

### **Key Steps in Fields Generation**

1. **Reading OpenAPI Spec:**  
   - Reads schema definitions from `SPEC_FILE_PATH`.
   - Focuses on schemas without underscores (filters `_base` schemas).

2. **Processing Base Fields:**  
   - Base schema references are extracted from `allOf` definitions.
   - Fields are copied from the base schema into the generated dataclass.
   - Field names are sanitized to be valid Python identifiers.

3. **Handling Nested Resources:**  
   - Nested resources are identified within the schema.
   - If a nested reference is found, the corresponding nested resource dataclass is created and included in the parent class.
   - Nested fields are marked as `Optional` and are postponed if dependencies exist.

4. **Topological Sorting:**  
   - Ensures that dataclasses are generated in the correct dependency order.
   - Handles cyclic dependencies by raising errors.

5. **Mapping to Endpoints:**  
   - Generates a mapping of fields to API responses using list and show schemas.
   - Outputs a `endpoint_field_mapping.json` file for later use in endpoint definitions.

---

### **Example Workflow in `fields.py`**

#### Input OpenAPI Schema Example

```json
"Account": {
    "allOf": [
        { "$ref": "#/components/schemas/BaseEntity" },
        {
            "properties": {
                "name": { "type": "string" },
                "contacts": {
                    "$ref": "#/components/schemas/Contact"
                }
            }
        }
    ]
},
"Contact": {
    "properties": {
        "email": { "type": "string" },
        "phone": { "type": "string" }
    }
}
```

#### Output Generated Dataclass

```python
from dataclasses import dataclass
from typing import Optional
from models.schemas import *

@dataclass
class Account_Fields:
    id: Optional[int] = None
    created_at: Optional[str] = None
    name: Optional[str] = None
    contacts: Optional[Contact_Fields] = None
```

---

### **Handling Base Fields**

1. **Base Schema Reference Processing:**  
   - Extracted from the first `allOf` item.
   - Fields from the referenced schema (e.g., `BaseEntity`) are added.

2. **Base Fields Example:**  

   ```python
   @dataclass
   class BaseEntity:
       id: Optional[int] = None
       created_at: Optional[str] = None
   ```

---

### **Handling Nested Resources**

1. **Detecting Nested Fields:**  
   - Any field containing a reference (`$ref`) to another schema is treated as a nested resource.
   - These are appended with `_Fields` and added to the parent dataclass.

2. **Nested Field Example:**

   ```python
   @dataclass
   class Contact_Fields:
       email: Optional[str] = None
       phone: Optional[str] = None
   ```

3. **Embedding in Parent:**

   ```python
   @dataclass
   class Account_Fields:
       name: Optional[str] = None
       contacts: Optional[Contact_Fields] = None
   ```

---

### **Mapping to Endpoints**

The generator script processes schemas with `_list` and `_show` suffixes to establish relationships between fields and endpoint responses.

**Example Mapping in `endpoint_field_mapping.json`:**

```json
{
    "Account_list": "Account_Fields",
    "User_show": "User_Fields"
}
```

**Logic:**  
- The mapping associates the API response schemas to the generated field dataclasses.
- Helps the endpoint generator (`endpoints.py`) link responses to correct models.

---

### 3. **Query Generator (`query.py`)**

**Purpose:**  
Generates dataclasses for API query parameters.

**Key Logic:**  
- Reads query parameters from API operations.
- Transforms query parameter names to valid Python identifiers.
- Maps OpenAPI types to Python types.
- Writes required and optional fields separately.

**Example Output:**

```python
@dataclass
class AccountQuery:
    account_id: int
    status: Optional[str] = None
```

---

### 4. **Request Body Generator (`request_body.py`)**

**Purpose:**  
Processes request body parameters for API operations.

**Key Logic:**  
- Extracts the request body schema from `application/json` content.
- Handles nested object properties.
- Generates dataclasses with required and optional fields.

**Example Output:**

```python
@dataclass
class CreateAccountRequestBody:
    name: str
    email: str
    age: Optional[int] = None
```

---

### 5. **Endpoints Generator (`endpoints.py`)**

**Purpose:**  
Creates an `Endpoints` registry to store endpoint mappings.

**Key Logic:**  
- Iterates through API paths and methods.
- Stores metadata such as path, method, query, and request body models.
- Handles special download cases based on HTTP 303 responses.

**Example Output:**

```python
class Endpoints:
    registry = {
        'get_user': {
            'path': '/users/{user_id}',
            'method': 'GET',
            'query_model': UserQuery,
            'request_body_model': None
        }
    }
```

---

## Running the Generator

To execute the generator and produce dataclasses, run:

```bash
python generate_models.py
```

This script will initialize the models directory, download the OpenAPI spec, and generate all necessary dataclasses.

---

## Directory Structure

```
project-root/
│-- models/
│   ├── query.py
│   ├── request_body.py
│   ├── endpoints.py
│   ├── fields.py
│   ├── schemas.py
│-- static/
│   ├── __init__.py
│   ├── models_registry.py
│-- generate_models.py
│-- openapi.json
```
**Static files get copied to models directory automatically before generating the model dataclasses**
---

## Conclusion

This setup automates the creation of Python dataclasses from an OpenAPI spec, providing a structured way to handle API interactions and ensuring maintainability through a clear generation flow.

