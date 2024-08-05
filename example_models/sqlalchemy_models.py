# File: model_schema_exporter/example_models/sqlalchemy_models.py
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SQLAlchemyExampleModel(Base):
    __tablename__ = 'example_model'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String)
    is_active = Column(Boolean, default=True)