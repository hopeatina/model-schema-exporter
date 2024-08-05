# File: tests/test_utils.py

class TestModel:
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields

class TestField:
    def __init__(self, name, field_type, nullable=False, unique=False, **kwargs):
        self.name = name
        self.field_type = field_type
        self.nullable = nullable
        self.unique = unique
        self.extra = kwargs

def create_test_model(framework):
    if framework == 'django':
        return TestModel('DjangoExampleModel', [
            TestField('id', 'AutoField', unique=True),
            TestField('name', 'CharField', max_length=100),
            TestField('description', 'TextField', nullable=True),
            TestField('is_active', 'BooleanField'),
            TestField('price', 'DecimalField', max_digits=10, decimal_places=2),
        ])
    elif framework == 'sqlalchemy':
        return TestModel('SQLAlchemyExampleModel', [
            TestField('id', 'Integer', primary_key=True),
            TestField('name', 'String', length=100),
            TestField('description', 'String', nullable=True),
            TestField('is_active', 'Boolean'),
            TestField('price', 'Numeric', precision=10, scale=2),
        ])
    elif framework == 'fastapi':
        return TestModel('FastAPIExampleModel', [
            TestField('id', 'int'),
            TestField('name', 'str'),
            TestField('description', 'str', nullable=True),
            TestField('is_active', 'bool'),
            TestField('price', 'float'),
        ])
    else:
        raise ValueError(f"Unsupported framework: {framework}")