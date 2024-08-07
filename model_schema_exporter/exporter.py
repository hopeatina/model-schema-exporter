import json
import logging

class ModelSchemaExporter:
    def __init__(self, models_data: dict):
        self.models_data = models_data
        self.logger = logging.getLogger(__name__)

    def generate_json(self) -> str:
        return json.dumps(self.models_data, indent=2)

    def export_to_file(self, filename: str):
        json_data = self.generate_json()
        with open(filename, 'w') as f:
            f.write(json_data)
        self.logger.info(f"Exported {len(self.models_data['models'])} models to {filename}")