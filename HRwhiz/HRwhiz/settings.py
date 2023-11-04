"""
Django settings for HRwhiz project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "django-insecure-t4viu=l@ghn(1ue3ge4p5^e+iuir7h@z!)k_=43f6oysj50v@3"

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True



SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', 'false').lower() == 'true'
DATABASE_URL = os.environ.get('DATABASE_URL')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(" ")


# Application definition

INSTALLED_APPS = [
    'render.apps.RenderConfig',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "employee",
    "manager",
    "HR"
    # 'rest_framework',
    # 'rest_framework.authtoken',
    # 'rest_framework_jwt',
    # 'corsheaders',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # 'corsheaders.middleware.CorsMiddleware',
]

# # Added
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
#     ),
# }
# CORS_ALLOW_ALL_ORIGINS = True

# # JWT settings
# from datetime import timedelta

# JWT_AUTH = {
#     'JWT_ALLOW_REFRESH': True,
#     'JWT_EXPIRATION_DELTA': timedelta(days=1),
#     'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=7),
# }
# # Till here

ROOT_URLCONF = "HRwhiz.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR, 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "HRwhiz.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

DATABASES['default'] = dj_database_url.parse('postgres://hrwhizdbuser:sQJ49ebjjGfkihCOJP0RCEg5Odb5QSkR@dpg-cl2t70pnovjs73b7chdg-a.oregon-postgres.render.com/hrwhizdb_53t8')


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
STATICFILES_DIRS  = ['static']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587  # Use 465 for SSL
EMAIL_USE_TLS = True  # Use False if you're using SSL
EMAIL_HOST_USER = 'hrwhizapp2023@gmail.com'
EMAIL_HOST_PASSWORD ='jyev jmcf dtzt bdrh'  # Your app password
