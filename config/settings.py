"""
Django settings for hokudai_furima project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('HOKUDAI_FURIMA_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hokudai_furima.account',
    'hokudai_furima.product',
    'hokudai_furima.search',
    'hokudai_furima.chat',
    'hokudai_furima.core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = (
    ('django.contrib.auth.backends.ModelBackend'),
)

#ROOT_URLCONF = 'hokudai_furima.urls'
ROOT_URLCONF = 'config.urls'

PROJECT_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_ROOT, 'templates')],
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

#WSGI_APPLICATION = 'hokudai_furima.wsgi.application'
WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

db_name = os.getenv('HOKUDAI_FURIMA_DB_NAME')
db_user = os.getenv('HOKUDAI_FURIMA_DB_USER')
db_pass = os.getenv('HOKUDAI_FURIMA_DB_PASSWORD')

DATABASES = { 'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': db_pass,
        'HOST': 'db',
        'PORT': 5432,
    }
}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

try:
    from .local_settings import *
except ImportError:
    pass

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    ('css', os.path.join(PROJECT_ROOT, 'hokudai_furima', 'static', 'css')),
    ('img', os.path.join(PROJECT_ROOT, 'hokudai_furima', 'static', 'img')),
    ('js', os.path.join(PROJECT_ROOT, 'hokudai_furima', 'static', 'js')),
)
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

AUTH_USER_MODEL = 'account.User'
LOGIN_REDIRECT_URL = '/account/'
LOGIN_URL = '/account/login/'
