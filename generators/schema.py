import os
import json
from pathlib import Path

SCHEMA_PATH = Path(os.getenv("SCHEMA_PATH", "models/schemas.py"))
SPEC_FILE_PATH =Path(os.getenv("SPEC_FILE_PATH"))

HEADER = """from dataclasses import dataclass
from typing import Optional, List, Literal
import datetime

"""

def sanitize_name(name: str) -> str:
    """Sanitize field names to make them valid Python identifiers."""
    return name.replace("-", "_").replace(".", "_").replace(" ", "_").replace("[", "_").replace("]", "_")

def map_property_type(field_schema: dict) -> str:
    """Map OpenAPI property types to Python types."""
    prop_type = field_schema.get("type", "any")
    format_type = field_schema.get("format", None)

    if prop_type == "integer":
        return "int"
    elif prop_type == "number":
        return "float"
    elif prop_type == "boolean":
        return "bool"
    elif prop_type == "string":
        if format_type == "date-time":
            return "datetime.datetime"
        elif format_type == "date":
            return "datetime.date"
        elif "enum" in field_schema:
            return f"Literal[{', '.join(repr(e) for e in field_schema['enum'])}]"
        return "str"
    elif prop_type == "array":
        items = field_schema.get("items", {})
        item_type = map_property_type(items)
        return f"List[{item_type}]"
    elif prop_type == "object":
        return "dict"
    return "Any"

def generate_schema_dataclass_code(schema_name: str, schema: dict) -> None:
    """
    Generate schema dataclass with proper type mappings, handling nested objects.
    """
    SCHEMA_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not SCHEMA_PATH.exists():
        with open(SCHEMA_PATH, "w") as f:
            f.write(HEADER)

    def process_schema(name: str, schema: dict, generated_classes: set) -> None:
        """
        Recursively process schema for nested objects, ensuring required fields
        are listed before optional fields.
        """
        if name in generated_classes:
            return  # Avoid duplicate generation
        generated_classes.add(name)

        dataclass_code = f"@dataclass\nclass {name}:\n"
        properties = schema.get("properties", {})
        required = set(schema.get("required", []))

        # Separate required and optional fields
        required_fields = {k: v for k, v in properties.items() if k in required}
        optional_fields = {k: v for k, v in properties.items() if k not in required}

        # Add required fields
        for field_name, field_schema in required_fields.items():
            if field_schema.get("type") == "object":
                nested_class_name = f"{name}_{sanitize_name(field_name).capitalize()}"
                process_schema(nested_class_name, field_schema, generated_classes)
                python_type = nested_class_name
            else:
                python_type = map_property_type(field_schema)

            sanitized_name = sanitize_name(field_name)
            dataclass_code += f"    {sanitized_name}: {python_type}\n"

        # Add optional fields
        for field_name, field_schema in optional_fields.items():
            if field_schema.get("type") == "object":
                nested_class_name = f"{name}_{sanitize_name(field_name).capitalize()}"
                process_schema(nested_class_name, field_schema, generated_classes)
                python_type = nested_class_name
            else:
                python_type = map_property_type(field_schema)

            sanitized_name = sanitize_name(field_name)
            dataclass_code += f"    {sanitized_name}: Optional[{python_type}] = None\n"

        if not properties:
            dataclass_code += "    pass\n"  # Handle empty classes

        dataclass_code += "\n"
        with open(SCHEMA_PATH, "a") as f:
            f.write(dataclass_code)

    formatted_class_name = schema_name
    process_schema(formatted_class_name, schema, set())

def generate_schema_dataclasses():
    input_file = SPEC_FILE_PATH  # Replace with your OpenAPI spec file path

    with open(input_file, "r") as f:
        spec = json.load(f)

    if "components" not in spec or "schemas" not in spec["components"]:
        print("No schemas found in the OpenAPI spec.")
        return

    schemas = spec["components"]["schemas"]

    for schema_name, schema in schemas.items():
        if "_base" in schema_name:  # Filter schemas containing '_base'
            generate_schema_dataclass_code(schema_name, schema)

    print(f"Dataclasses generated in {SCHEMA_PATH}")
    
if __name__ == "__main__":
    generate_schema_dataclasses()
