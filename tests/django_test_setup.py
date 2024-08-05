# File: tests/django_test_setup.py

import os
import django
from django.conf import settings

def setup_django_test_environment():
    settings.configure(
        DEBUG=True,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        INSTALLED_APPS=[
            'tests.test_app',  # Our test app
        ],
        USE_TZ=True,
        TIME_ZONE='UTC',
    )

    django.setup()