import click
from model_schema_exporter.exporter import ModelSchemaExporter

@click.command()
@click.argument('framework', type=click.Choice(['django', 'sqlalchemy', 'fastapi']))
@click.argument('app_module')
@click.argument('output', type=click.Path())
@click.option('--pretty', is_flag=True, help="Output pretty-printed JSON")
def main(framework, app_module, output, pretty):
    """Export model schemas to JSON.

    FRAMEWORK: The web framework used (django, sqlalchemy, or fastapi)
    APP_MODULE: The Python module containing your models
    OUTPUT: The output JSON file path
    """
    try:
        exporter = ModelSchemaExporter(framework, app_module)
        exporter.extract_models()
        
        if pretty:
            json_data = exporter.generate_json()
            with open(output, 'w') as f:
                f.write(json_data)
        else:
            exporter.export_to_file(output)
        
        click.echo(f"Model schemas exported to {output}")
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)
        raise click.Abort()

if __name__ == "__main__":
    main()