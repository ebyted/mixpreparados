# config/settings/dev.py
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mixpreparados_db',
        'USER': 'postgres',
        'PASSWORD': 'shivah',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

