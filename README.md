# Model Schema Exporter

Model Schema Exporter is a versatile Python tool that extracts model schemas from Django, Flask, and FastAPI applications and exports them to JSON format. This tool is particularly useful for developers who need to visualize their data models or integrate them with other tools.

## Installation

You can install Model Schema Exporter using pip:

```bash
pip install model-schema-exporter
```

## Usage

Model Schema Exporter can be used as a command-line tool:

```bash
model-schema-exporter <framework> <output_file> [OPTIONS]
```

- `<framework>`: The web framework you're using. Choose from 'django', 'flask', or 'fastapi'.
- `<output_file>`: The path where the output JSON file will be saved.

### Options

- `--app-label`: (Django only) Specify a particular Django app to extract models from.
- `--project-root PATH`: Specify the root directory of your project. If not provided, the current working directory is used as the default.
- `--verbose`: Enable verbose logging for more detailed output.

### Examples

1. For a Django project (all apps):

```bash
model-schema-exporter django output.json --project-root /path/to/your/project
```

2. For a Django project (specific app):

```bash
model-schema-exporter django output.json --app-label myapp --project-root /path/to/your/project
```

3. For a Flask project:

```bash
model-schema-exporter flask output.json --project-root /path/to/your/project
```

4. For a FastAPI project:

```bash
model-schema-exporter fastapi output.json --project-root /path/to/your/project
```

## How It Works

Model Schema Exporter uses framework-specific shell scripts to extract model information:

1. `extract_django_models.sh`: Extracts models from Django projects.
2. `extract_flask_models.sh`: Extracts models from Flask projects using SQLAlchemy.
3. `extract_fastapi_models.sh`: Extracts Pydantic models from FastAPI projects.

These scripts are executed in the context of your project, ensuring that all project-specific configurations and environment variables are respected.

## Project Root

The `--project-root` option allows you to specify the root directory of your project. This is crucial for the tool to locate your project files and execute the extraction scripts correctly.

- If not specified, the current working directory is used as the project root.
- The project root is typically:
  - For Django: The directory containing `manage.py`
  - For Flask/FastAPI: The directory containing your main application file (e.g., `app.py` or `main.py`)

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
- You can extract models from all apps or specify a particular app using the `--app-label` option.

### Flask

- Make sure your models are defined using SQLAlchemy and are importable from your main application file.

### FastAPI

- Ensure your Pydantic models are importable from your main application file.

## Troubleshooting

If you encounter issues:

1. Ensure you're running the command from your project's root directory, or use the `--project-root` option.
2. Check that your project's virtual environment is activated.
3. For Django projects, make sure your `DJANGO_SETTINGS_MODULE` environment variable is correctly set.
4. Run the exporter with the `--verbose` flag for more detailed logging:

```bash
model-schema-exporter django output.json --project-root /path/to/your/project --verbose
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
