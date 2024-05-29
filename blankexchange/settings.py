"""
Django settings for blankexchange project.

Generated by 'django-admin startproject' using Django 4.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
# configuration settings
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-cikg1lw$219%t5l=6lz*dj#bi$@3456iz2h6p%oj7p$ngq$&uh'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = False


ALLOWED_HOSTS = ['192.168.186.107','*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third party app
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'drf_yasg',
    'dj_rest_auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # custom apps
    'core_app_root',
    'core_app_root.security',
    'core_app_root.security.user',
    'core_app_root.security.auth',
    'core_app_root.user_services',
    'core_app_root.user_services.bankmanagement',
    'core_app_root.user_services.wallet_app',
    'whitenoise.runserver_nostatic'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'allauth.account.middleware.AccountMiddleware'
]

ROOT_URLCONF = 'blankexchange.urls'

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

WSGI_APPLICATION = 'blankexchange.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'blancexchangedb',
#         'USER': 'blancexchangedbuser',
#         'PASSWORD': 'Blancexchange$',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT=os.path.join(BASE_DIR,'static')

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import os
# STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
# STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
    'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework_simplejwt.authentication.JWTAuthentication',
    'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    'rest_framework.authentication.SessionAuthentication',
    'rest_framework.authentication.BasicAuthentication',
    ),

    'DEFAULT_FILTER_BACKENDS':
    ['django_filters.rest_framework.DjangoFilterBackend'],
}
SPECTACULAR_SETTINGS = {
    'TITLE': 'Blankexchange API',
    'DESCRIPTION': 'Blankexchange Documentation',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}
AUTH_USER_MODEL = 'core_app_root_security_user.User'
# configure Djoser
DJOSER = {
    "USER_ID_FIELD": "username",
    "LOGIN_FIELD": "email",
    "SEND_ACTIVATION_EMAIL": True,
    "ACTIVATION_URL": "activate/{uid}/{token}",
    "PASSWORD_RESET_CONFIRM_URL": "reset_password/{uid}/{token}", # the reset link 
    'SERIALIZERS': {
        'token_create': 'apps.accounts.serializers.CustomTokenCreateSerializer',
    },
}
CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",
#     "http://127.0.0.1:3000",
#     "https://react-ts.csb.app",
#     "https://cbastudyapp.com",
#     "https://www.cbastudyapp.com",
#     'http://127.0.0.1:5500',
#     'http://localhost:8000'
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend" # new
SITE_ID = 1 
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
