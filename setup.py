from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="model-schema-exporter",
    version="0.1.0",
    author="Hope Atina",
    author_email="",
    description="A tool to export model schemas from Django, SQLAlchemy, and FastAPI to JSON",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/model-schema-exporter",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    install_requires=[
        "click",
        "django",
        "sqlalchemy",
        "fastapi",
        "pydantic",
    ],
    entry_points={
        "console_scripts": [
            "model-schema-exporter=model_schema_exporter.cli:main",
        ],
    },
)