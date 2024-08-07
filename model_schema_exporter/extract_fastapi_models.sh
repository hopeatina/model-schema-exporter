#!/bin/bash
# extract_fastapi_models.sh

python <<EOF
import json
import sys
import os
from importlib import import_module

# Add the project root to the Python path
sys.path.insert(0, os.getcwd())

# Import the Pydantic models (adjust the import path as needed)
models_module = import_module('app.models')

models_data = []
for name, obj in models_module.__dict__.items():
    if isinstance(obj, type) and hasattr(obj, '__fields__'):
        model_data = {
            "name": name,
            "fields": []
        }
        for field_name, field in obj.__fields__.items():
            field_data = {
                "name": field_name,
                "type": str(field.type_),
                "nullable": field.allow_none,
                "unique": False,  # Pydantic doesn't have built-in unique constraints
            }
            model_data["fields"].append(field_data)
        models_data.append(model_data)

print(json.dumps({"models": models_data}, indent=2))
EOF