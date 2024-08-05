# File: tests/mock_models.py
class MockDjangoModel:
    def __init__(self, **fields):
        self._meta = MockMeta()
        for name, value in fields.items():
            setattr(self._meta, name, value)

class MockMeta:
    def __init__(self):
        self.fields = []

class MockField:
    def __init__(self, name, field_type, null=False, unique=False, max_length=None, max_digits=None, decimal_places=None):
        self.name = name
        self.field_type = field_type
        self.null = null
        self.unique = unique
        self.max_length = max_length
        self.max_digits = max_digits
        self.decimal_places = decimal_places

# Mock Django model
class MockDjangoExampleModel(MockDjangoModel):
    def __init__(self):
        super().__init__(
            fields=[
                MockField('id', 'AutoField', null=False, unique=True),
                MockField('name', 'CharField', null=False, unique=False, max_length=100),
                MockField('description', 'TextField', null=True, unique=False),
                MockField('is_active', 'BooleanField', null=False, unique=False),
                MockField('price', 'DecimalField', null=False, unique=False, max_digits=10, decimal_places=2),
            ]
        )

# Mock SQLAlchemy model
class MockSQLAlchemyExampleModel:
    __tablename__ = 'example_model'
    id = 'Column(Integer, primary_key=True)'
    name = 'Column(String(100))'
    description = 'Column(String)'
    is_active = 'Column(Boolean, default=True)'

# Mock FastAPI (Pydantic) model
class MockFastAPIExampleModel:
    id: int
    name: str
    description: str = None
    is_active: bool = True

    @classmethod
    def __fields__(cls):
        return {
            'id': MockField('id', 'int', null=False, unique=True),
            'name': MockField('name', 'str', null=False, unique=False),
            'description': MockField('description', 'str', null=True, unique=False),
            'is_active': MockField('is_active', 'bool', null=False, unique=False),
        }