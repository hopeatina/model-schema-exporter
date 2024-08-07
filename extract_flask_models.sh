#!/bin/bash
# extract_flask_models.sh

python <<EOF
import json
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.getcwd())

# Import the Flask app and SQLAlchemy models
from app import db

models_data = []
for name, obj in db.Model._decl_class_registry.items():
    if isinstance(obj, type) and issubclass(obj, db.Model):
        model_data = {
            "name": name,
            "fields": []
        }
        for column in obj.__table__.columns:
            field_data = {
                "name": column.name,
                "type": str(column.type),
                "nullable": column.nullable,
                "unique": column.unique,
            }
            model_data["fields"].append(field_data)
        models_data.append(model_data)

print(json.dumps({"models": models_data}, indent=2))
EOF