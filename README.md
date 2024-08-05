# Model Schema Exporter

Model Schema Exporter is a versatile Python tool that extracts model schemas from Django, SQLAlchemy, and FastAPI applications and exports them to JSON format. This tool is particularly useful for developers who need to visualize their data models or integrate them with other tools.

## Installation

You can install Model Schema Exporter using pip:

```bash
pip install model-schema-exporter
```

## Usage

Model Schema Exporter can be used as a command-line tool:

```bash
model-schema-exporter <framework> <app_module> <output_file>
```

- `<framework>`: The web framework you're using. Choose from 'django', 'sqlalchemy', or 'fastapi'.
- `<app_module>`: The Python module containing your models.
- `<output_file>`: The path where the output JSON file will be saved.

### Options

- `--pretty`: Output pretty-printed JSON for better readability.

### Examples

1. For a Django project:

```bash
model-schema-exporter django myproject.myapp.models output.json
```

2. For a SQLAlchemy project:

```bash
model-schema-exporter sqlalchemy myproject.models output.json
```

3. For a FastAPI project using Pydantic models:

```bash
model-schema-exporter fastapi myproject.models output.json
```

## Output Format

The tool generates a JSON file with the following structure:

```json
{
  "models": [
    {
      "name": "ModelName",
      "fields": [
        {
          "name": "field_name",
          "type": "FieldType",
          "nullable": true,
          "unique": false
        }
        // ... more fields
      ]
    }
    // ... more models
  ]
}
```

## Framework-specific Notes

### Django

- Ensure your Django settings are properly configured.
- The tool will automatically discover all models in your Django project.

### SQLAlchemy

- Make sure your models are defined using the declarative base.
- The tool will find all classes that inherit from the SQLAlchemy declarative base.

### FastAPI

- Your Pydantic models should be importable from the specified module.
- The tool will extract all classes that inherit from `pydantic.BaseModel`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
