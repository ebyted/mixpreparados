from .base import *

DEBUG = False

ALLOWED_HOSTS = ['elcompadremix.com', 'www.elcompadremix.com']

CSRF_TRUSTED_ORIGINS = [
    'https://elcompadremix.com',
    'https://www.elcompadremix.com',
]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST', default='db'),
        'PORT': env('POSTGRES_PORT', default='5432'),
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'ERROR',
    },
}