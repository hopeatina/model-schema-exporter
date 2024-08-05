# File: model_schema_exporter/example_models/django_models.py
from django.db import models

class DjangoExampleModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    is_active = models.BooleanField(default=True)