# File: tests/test_app/models.py

from django.db import models

class DjangoExampleModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'test_app'