import json
import importlib
import inspect
from typing import List, Dict, Any

class ModelSchemaExporter:
    def __init__(self, framework: str, app_module: str, test_mode: bool = False):
        self.framework = framework.lower()
        self.app_module = app_module
        self.models = []
        self.test_mode = test_mode

    def extract_models(self):
        module = importlib.import_module(self.app_module)
        if self.framework == 'sqlalchemy':
            self._extract_sqlalchemy_models(module)
        elif self.framework == 'fastapi':
            self._extract_fastapi_models(module)
        elif self.framework == 'django':
            self._extract_django_models(module)
        else:
            raise ValueError(f"Unsupported framework: {self.framework}")

    def _extract_sqlalchemy_models(self, module):
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and hasattr(obj, '__tablename__'):
                self.models.append(obj)

    def _extract_fastapi_models(self, module):
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and hasattr(obj, '__fields__'):
                self.models.append(obj)

    def _extract_django_models(self, module):
        if self.test_mode:
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, getattr(module, 'MockDjangoModel', object)):
                    self.models.append(obj)
        else:
            from django.apps import apps
            self.models = apps.get_models()

    def generate_json(self) -> str:
        model_data = []
        for model in self.models:
            model_info = {
                "name": model.__name__,
                "fields": self._get_model_fields(model)
            }
            model_data.append(model_info)
        
        return json.dumps({"models": model_data}, indent=2)

    def _get_model_fields(self, model) -> List[Dict[str, Any]]:
        if self.framework == 'django':
            return self._get_django_fields(model)
        elif self.framework == 'sqlalchemy':
            return self._get_sqlalchemy_fields(model)
        elif self.framework == 'fastapi':
            return self._get_fastapi_fields(model)

    def _get_django_fields(self, model):
        fields = []
        for field in model._meta.fields:
            field_info = {
                "name": field.name,
                "type": self._get_django_field_type(field),
                "nullable": field.null,
                "unique": field.unique,
            }
            fields.append(field_info)
        return fields

    def _get_django_field_type(self, field):
        from django.db import models
        
        type_mapping = {
            models.AutoField: "AutoField",
            models.BigIntegerField: "BigInteger",
            models.BooleanField: "Boolean",
            models.CharField: lambda f: f"CharField(max_length={f.max_length})",
            models.DateField: "Date",
            models.DateTimeField: "DateTime",
            models.DecimalField: lambda f: f"Decimal(max_digits={f.max_digits}, decimal_places={f.decimal_places})",
            models.EmailField: "Email",
            models.FileField: "File",
            models.FloatField: "Float",
            models.ImageField: "Image",
            models.IntegerField: "Integer",
            models.JSONField: "JSON",
            models.TextField: "Text",
            models.TimeField: "Time",
            models.URLField: "URL",
            models.UUIDField: "UUID",
        }

        for field_class, type_name in type_mapping.items():
            if isinstance(field, field_class):
                return type_name(field) if callable(type_name) else type_name
        
        return field.__class__.__name__

    def _get_sqlalchemy_fields(self, model):
        fields = []
        for name, value in model.__dict__.items():
            if not name.startswith('_'):
                field_info = {
                    "name": name,
                    "type": value,
                    "nullable": 'nullable=True' in value,
                    "unique": 'unique=True' in value,
                }
                fields.append(field_info)
        return fields

    def _get_fastapi_fields(self, model):
        fields = []
        for name, field in model.__fields__().items():
            field_info = {
                "name": field.name,
                "type": field.field_type,
                "nullable": field.null,
                "unique": field.unique,
            }
            fields.append(field_info)
        return fields

    def export_to_file(self, filename: str):
        json_data = self.generate_json()
        with open(filename, 'w') as f:
            f.write(json_data)

    def _get_django_field_type(self, field):
        if self.test_mode:
            return field.field_type  # For mock fields, we'll use the field_type directly
        else:
            # This is the original logic for real Django fields
            from django.db import models
            
            type_mapping = {
                models.AutoField: "AutoField",
                models.BigIntegerField: "BigInteger",
                models.BooleanField: "Boolean",
                models.CharField: lambda f: f"CharField(max_length={f.max_length})",
                models.DateField: "Date",
                models.DateTimeField: "DateTime",
                models.DecimalField: lambda f: f"Decimal(max_digits={f.max_digits}, decimal_places={f.decimal_places})",
                models.EmailField: "Email",
                models.FileField: "File",
                models.FloatField: "Float",
                models.ImageField: "Image",
                models.IntegerField: "Integer",
                models.JSONField: "JSON",
                models.TextField: "Text",
                models.TimeField: "Time",
                models.URLField: "URL",
                models.UUIDField: "UUID",
            }

            for field_class, type_name in type_mapping.items():
                if isinstance(field, field_class):
                    return type_name(field) if callable(type_name) else type_name
            
            return field.__class__.__name__
# Helper function to get all subclasses of a class
def get_all_subclasses(cls):
    all_subclasses = []
    for subclass in cls.__subclasses__():
        all_subclasses.append(subclass)
        all_subclasses.extend(get_all_subclasses(subclass))
    return all_subclasses