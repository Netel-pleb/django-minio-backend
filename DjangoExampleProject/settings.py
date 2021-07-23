"""
Django settings for DjangoExampleProject project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import distutils.util
from datetime import timedelta
from typing import List, Tuple

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sp1d7_7z9))q58(6k&1)9m_@!8e420*m+3dasq-*711fu8)y!6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_minio_backend.apps.DjangoMinioBackendConfig',  # Driver
    'DjangoExampleApplication',  # Test App
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

ROOT_URLCONF = 'DjangoExampleProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'DjangoExampleProject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'django_minio_backend.models.MinioBackendStatic'
DEFAULT_FILE_STORAGE = 'django_minio_backend.models.MinioBackend'

# #################### #
# django_minio_backend #
# #################### #

dummy_policy = {"Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "",
                        "Effect": "Allow",
                        "Principal": {"AWS": "*"},
                        "Action": "s3:GetBucketLocation",
                        "Resource": f"arn:aws:s3:::django-backend-dev-private"
                    },
                    {
                        "Sid": "",
                        "Effect": "Allow",
                        "Principal": {"AWS": "*"},
                        "Action": "s3:ListBucket",
                        "Resource": f"arn:aws:s3:::django-backend-dev-private"
                    },
                    {
                        "Sid": "",
                        "Effect": "Allow",
                        "Principal": {"AWS": "*"},
                        "Action": "s3:GetObject",
                        "Resource": f"arn:aws:s3:::django-backend-dev-private/*"
                    }
                ]}

MINIO_ENDPOINT = os.getenv("GH_MINIO_ENDPOINT", "play.min.io")
MINIO_EXTERNAL_ENDPOINT = os.getenv("GH_MINIO_EXTERNAL_ENDPOINT", "externalplay.min.io")
MINIO_EXTERNAL_ENDPOINT_USE_HTTPS = bool(distutils.util.strtobool(os.getenv("GH_MINIO_EXTERNAL_ENDPOINT_USE_HTTPS", "true")))
MINIO_ACCESS_KEY = os.getenv("GH_MINIO_ACCESS_KEY", "Q3AM3UQ867SPQQA43P2F")
MINIO_SECRET_KEY = os.getenv("GH_MINIO_SECRET_KEY", "zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG")
MINIO_USE_HTTPS = bool(distutils.util.strtobool(os.getenv("GH_MINIO_USE_HTTPS", "true")))
MINIO_PRIVATE_BUCKETS = [
    'django-backend-dev-private',
    'my-media-files-bucket',
]
MINIO_PUBLIC_BUCKETS = [
    'django-backend-dev-public',
    't5p2g08k31',
    '7xi7lx9rjh',
    'my-static-files-bucket',
]
MINIO_URL_EXPIRY_HOURS = timedelta(days=1)  # Default is 7 days (longest) if not defined
MINIO_CONSISTENCY_CHECK_ON_START = True
MINIO_POLICY_HOOKS: List[Tuple[str, dict]] = [
    # ('django-backend-dev-private', dummy_policy)
]
MINIO_MEDIA_FILES_BUCKET = 'my-media-files-bucket'  # replacement for STATIC_ROOT
MINIO_STATIC_FILES_BUCKET = 'my-static-files-bucket'  # replacement for MEDIA_ROOT
MINIO_BUCKET_EXISTENCE_CHECK_BEFORE_SAVE = True  # Create bucket if missing, then save
