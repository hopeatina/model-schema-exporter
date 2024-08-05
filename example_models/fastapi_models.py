# File: model_schema_exporter/example_models/fastapi_models.py
from pydantic import BaseModel
from typing import Optional

class FastAPIExampleModel(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    is_active: bool = True