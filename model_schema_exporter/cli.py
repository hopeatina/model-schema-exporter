import click
import logging
import subprocess
import json
import os
from model_schema_exporter.exporter import ModelSchemaExporter

@click.command()
@click.argument('framework', type=click.Choice(['django', 'flask', 'fastapi']))
@click.option('--app-label', help="Django app label to extract models from (optional, Django only)")
@click.option('--project-root', type=click.Path(exists=True), default='.', help="Path to the project root")
@click.option('--output', type=click.Path(), default='models.json')
@click.option('--verbose', is_flag=True, help="Enable verbose logging")
def main(framework, app_label, project_root, output, verbose):
    """Extract and export model schemas to JSON for Django, Flask, or FastAPI projects."""
    log_level = logging.INFO if verbose else logging.WARNING
    logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')

    logger = logging.getLogger(__name__)
    
    try:
        # Step 1: Extract models using the appropriate shell script
        logger.info(f"Extracting {framework} models")
        if framework == 'django':
            script_name = 'extract_django_models.sh'
            cmd = [f'./{script_name}']
            if app_label:
                cmd.append(app_label)
        elif framework == 'flask':
            script_name = 'extract_flask_models.sh'
            cmd = [f'./{script_name}']
        elif framework == 'fastapi':
            script_name = 'extract_fastapi_models.sh'
            cmd = [f'./{script_name}']
        
        result = subprocess.run(cmd, cwd=project_root, capture_output=True, text=True, check=True)
        models_json = result.stdout

        # Step 2: Process the extracted models
        logger.info("Processing extracted models")
        exporter = ModelSchemaExporter(json.loads(models_json))
        
        logger.info("Exporting to file")
        exporter.export_to_file(output)
        
        logger.info(f"Model schemas exported to {output}")
        click.echo(f"Successfully exported model schemas to {output}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Error running model extraction: {e}")
        logger.error(f"Script output: {e.output}")
        click.echo(f"Error: Failed to extract models", err=True)
        raise click.Abort()
    except Exception as e:
        logger.error(f"Error: {str(e)}", exc_info=True)
        click.echo(f"Error: {str(e)}", err=True)
        raise click.Abort()

if __name__ == "__main__":
    main()