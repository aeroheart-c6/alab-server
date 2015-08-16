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
)
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'cities_light',
    'django_js_reverse',
    'social.apps.django_app.default',
    'easy_thumbnails'
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
                # social auth context_processors
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
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
# DJANGO CITIES LIGHT
#--------------------------------------------------
CITIES_LIGHT_INCLUDE_COUNTRIES = ['PH']


#--------------------------------------------------
# Social Auth Settings
#--------------------------------------------------
AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.instagram.InstagramOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# Facebook Keys
FACEBOOK_KEY = '857915070962991'
FACEBOOK_SECRET = 'd0f0719250a1df402d8efa242ebd613f'
FACEBOOK_ACCESS_TOKEN = 'CAAMMROsNXS8BADq7cdSNHufvaDivlZBJlU4jwzcdBJqR1XWL7Lst4driVuZB8J3FnwRZCWhGZBBZBZCXuGQT97Pfy8V6B6tlGt7Yzoh4TBtWpjkUbxXdKAsZCZCRf8qYt0Kvk2XeXz1DmvDBAL2F0WQWQvK8pUZBApIHrcIrLZCtsIGE27SJJNTzdjsHiyZAJ7plkegOtZA39jscFgZDZD'
SOCIAL_AUTH_FACEBOOK_KEY = FACEBOOK_KEY
SOCIAL_AUTH_FACEBOOK_SECRET = FACEBOOK_SECRET
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

# Instagram Keys
INSTAGRAM_KEY = 'f8654f82b130433cbad0c32a044d7b5e'
INSTAGRAM_SECRET = '66436661ebe44537958c3dd97db05104'
INSTAGRAM_REDIRECT = 'http://localhost:8000/complete/instagram/'
SOCIAL_AUTH_INSTAGRAM_KEY = INSTAGRAM_KEY
SOCIAL_AUTH_INSTAGRAM_SECRET = INSTAGRAM_SECRET
SOCIAL_AUTH_INSTAGRAM_REDIRECT_URL = INSTAGRAM_REDIRECT

# social auth steps
SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'users.pipeline.create_profile',
)


#--------------------------------------------------
# Easy Thumbnail Config
#--------------------------------------------------
THUMBNAIL_ALIASES = {
    '': {
        'avatar': {'size': (100, 100), 'crop': True},
        'thumbnail_avatar': {'size': (25, 25), 'crop': True},
        'organization_photo': {'size': (300, 300), 'crop': True},
        'thumbnail_activity': {'size': (45, 45), 'crop': True},


    },
}


#--------------------------------------------------
# Overrides / Bootstrap Code
#--------------------------------------------------
from .local import *


