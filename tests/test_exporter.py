# File: tests/test_exporter.py

import unittest
import json
from django.test import TestCase
from model_schema_exporter.exporter import ModelSchemaExporter
from tests.django_test_setup import setup_django_test_environment

# Set up the Django test environment
setup_django_test_environment()

# Now it's safe to import Django models
from tests.test_app.models import DjangoExampleModel

class TestModelSchemaExporter(TestCase):
    def setUp(self):
        self.django_exporter = ModelSchemaExporter('django', 'tests.test_app.models')

    def test_django_model_extraction(self):
        self.django_exporter.extract_models()
        self.assertEqual(len(self.django_exporter.models), 1)
        self.assertEqual(self.django_exporter.models[0].__name__, 'DjangoExampleModel')

    def test_generate_json(self):
        self.django_exporter.extract_models()
        json_output = self.django_exporter.generate_json()
        data = json.loads(json_output)
        
        self.assertIn('models', data)
        self.assertEqual(len(data['models']), 1)
        self.assertEqual(data['models'][0]['name'], 'DjangoExampleModel')
        
        fields = {field['name']: field for field in data['models'][0]['fields']}
        self.assertEqual(fields['id']['type'], 'AutoField')
        self.assertEqual(fields['name']['type'], 'CharField(max_length=100)')
        self.assertEqual(fields['description']['type'], 'Text')
        self.assertEqual(fields['is_active']['type'], 'Boolean')
        self.assertEqual(fields['price']['type'], 'Decimal(max_digits=10, decimal_places=2)')

if __name__ == '__main__':
    unittest.main()