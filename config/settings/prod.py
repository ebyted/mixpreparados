# config/settings/prod.py
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['elcompadremix.com, www.elcompadremix.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': 'db',  # Docker
        'PORT': '5432',
    }
}
