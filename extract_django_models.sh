#!/bin/bash
# extract_django_models.sh

if [ $# -eq 1 ]; then
    app_label="$1"
    python_command="app_config = apps.get_app_config('$app_label'); models = app_config.get_models()"
else
    python_command="models = apps.get_models()"
fi

python manage.py shell <<EOF
import json
from django.apps import apps

$python_command

models_data = []
for model in models:
    model_data = {
        "name": model.__name__,
        "app_label": model._meta.app_label,
        "fields": []
    }
    for field in model._meta.fields:
        field_data = {
            "name": field.name,
            "type": field.get_internal_type(),
            "nullable": field.null,
            "unique": field.unique,
        }
        model_data["fields"].append(field_data)
    models_data.append(model_data)

print(json.dumps({"models": models_data}, indent=2))
EOF