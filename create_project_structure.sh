#!/bin/bash

# Navigate to the project directory
cd /Users/hopeatina/Documents/model-schema-exporter

# Create main package directory
mkdir -p model_schema_exporter

# Create test directory
mkdir -p tests

# Create main package files
touch model_schema_exporter/__init__.py
touch model_schema_exporter/exporter.py
touch model_schema_exporter/cli.py

# Create test files
touch tests/__init__.py
touch tests/test_exporter.py
touch tests/test_cli.py

# Create root level files
touch README.md
touch LICENSE
touch setup.py
touch requirements.txt
touch .gitignore

# Add some initial content to .gitignore
echo "*.pyc" >> .gitignore
echo "__pycache__" >> .gitignore
echo "*.egg-info" >> .gitignore
echo "dist" >> .gitignore
echo "build" >> .gitignore

echo "Project structure created successfully!"