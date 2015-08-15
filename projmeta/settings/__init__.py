from __future__ import (
    absolute_import,
)

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+_5^j+5x@%-_#if&5dd@()1ldv)@81r%him*j4y^rk&a*)#fa^'


ALLOWED_HOSTS = []
APPEND_SLASH = False
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'basic': {
            'format': '[%(asctime)s %(levelname)s] %(name)s: %(message)s',
        }
    },

    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'basic',
        },
        'logfile': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'basic',
            'filename': os.path.join(BASE_DIR, 'var', 'logs', 'debug.log'),
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 10,
        },
    },

    'loggers': {
        'default': {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    },
}


#--------------------------------------------------
# Application Definition
#--------------------------------------------------
WSGI_APPLICATION = 'projcore.wsgi.application'
ROOT_URLCONF = 'projcore.urls'
AUTH_USER_MODEL = 'users.User'
LOGIN_URL = 'users:login'
LOGIN_REDIRECT_URL = 'users:index'

INTERNAL_APPS = (
    'security',
    'users',
    'organizations',
    'activities',
    'vending',

    'django_js_reverse',
)
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
) + INTERNAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (
            os.path.join(BASE_DIR, 'frontend', 'templates'),
        ),
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


#--------------------------------------------------
# Persistence
#--------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'alab',
        'USER': '',
        'PASSWORD': '',
    }
}


#--------------------------------------------------
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
#--------------------------------------------------
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


#--------------------------------------------------
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
#--------------------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'frontend', 'static.prod')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'frontend', 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'frontend', 'media')


#--------------------------------------------------
# Overrides / Bootstrap Code
#--------------------------------------------------
from .local import *
