import click
from .exporter import ModelSchemaExporter

@click.command()
@click.argument('framework', type=click.Choice(['django', 'sqlalchemy', 'fastapi']))
@click.argument('app_module')
@click.argument('output')
def main(framework, app_module, output):
    """Export model schemas to JSON."""
    exporter = ModelSchemaExporter(framework, app_module)
    exporter.extract_models()
    exporter.export_to_file(output)
    click.echo(f"Model schemas exported to {output}")

if __name__ == "__main__":
    main()