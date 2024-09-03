"""
Django settings for auth_app project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
# import os
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-q&=86$qb(vo$dc1f1_#124-eb27_n_$c1cuavzg)z8e6!j5uky'

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
    #third party 
    'auth_app',
    'auth_app_user',
    'models_app',
    'city_state_app',

    # jwt
    'rest_framework_simplejwt',

    # google auth
    'google_app',

    'django.contrib.sites',          # Required for allauth
    'allauth',                        # Required for allauth
    'allauth.account',                # For email and username login
    'allauth.socialaccount',          # For social authentication
    'allauth.socialaccount.providers.google',  # Google provider

    # email otp
    'rest_framework',  # this is for email

]
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'social_django.middleware.SocialAuthExceptionMiddleware',    # add this is for google auth
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'auth_app.urls'

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

                'social_django.context_processors.backends', # add this is for google auth
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'auth_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('DB_NAME'),                      
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': config('DB_PORT'),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# abstract user=============================>
AUTH_USER_MODEL='auth_app_user.User'

# ==========================================>

# jwt ====================================>
from datetime import timedelta


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication', #email_otp
    )
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=300),  # Access token expiration time
    'REFRESH_TOKEN_LIFETIME': timedelta(days=365),    # Refresh token expiration time
    'ROTATE_REFRESH_TOKENS': False,  # Whether to rotate refresh tokens
    'BLACKLIST_AFTER_ROTATION': True, # Whether to blacklist tokens after rotation
    'ALGORITHM': 'HS256',             # Algorithm used for encoding the token
    'SIGNING_KEY': SECRET_KEY,        # The key used to sign the JWT
    'VERIFYING_KEY': None,            # The key used to verify the JWT
    'AUTH_HEADER_TYPES': ('Bearer',), # The type of authentication in the header
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'USER_ID_FIELD': 'id',            # The field used to identify users
    'USER_ID_CLAIM': 'user_id',
    'AUTH_COOKIE': 'access_token',    # The name of the cookie to store the access token
    'AUTH_COOKIE_SECURE': True,       # Whether the cookie should only be sent over HTTPS
    'AUTH_COOKIE_HTTP_ONLY': True,    # Whether the cookie is HTTP only
    'AUTH_COOKIE_PATH': '/',          # The path for the cookie
    'AUTH_COOKIE_SAMESITE': 'Lax',    # The samesite setting for the cookie
}



# social app custom setting google

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

LOGIN_REDIRECT_URL = config('LOGIN_REDIRECT_URL')
LOGOUT_REDIRECT_URL = '/accounts/login/'

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': config('CLIENT_ID'),
            'secret': config('SECRET'),
            'key': ''

        },
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
    }
}

ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_EMAIL_REQUIRED = True


# for email opt step

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')