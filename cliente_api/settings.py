"""
Django settings for cliente_api project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ap$5r!x6_b9mlnwfbkn-!7iv($2(!4sa4a3+0y$zn@p6r40kk^'

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
    'social.apps.django_app.default',
    'login',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'cliente_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'cliente_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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

#backends for auth

AUTHENTICATION_BACKENDS = (
                'social.backends.twitter.TwitterOAuth',
                'django.contrib.auth.backends.ModelBackend',)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/home/'
LOGOUT_URL = 'logout/'

SOCIAL_AUTH_TWITTER_KEY = 'QOIzU991dfFzzQLWl0k9OydFM'
SOCIAL_AUTH_TWITTER_SECRET = '64UegKJt2y06Z1k5Mf1xyic8qzBPSv5xrovBTyeleELCPik2mp'

TWITTER_ACCESS_TOKEN = '732223243210391552-OstZefiDM03AtYPeZ7YQEjjU5ovJFhr'
TWITTER_ACCESS_TOKEN_SECRET = 'kgt4xBruNhpI0C0WiPqQBubZEWfsDSWJuAWJn8APNUvSX'

SOCIAL_AUTH_PIPELINE = (
    # recibe vía backend y uid las instancias de social_user y user
    'social.pipeline.social_auth.social_details',

    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',

    # Recibe según user.email la instancia del usuario y lo reemplaza con uno que recibió anteriormente
    'social.pipeline.social_auth.social_user',

    # Trata de crear un username válido según los datos que recibe
    'social.pipeline.user.get_username',

    # Crea un usuario nuevo si uno todavía no existe
    'social.pipeline.user.create_user',

    # Trata de conectar las cuentas
    'social.pipeline.social_auth.associate_user',

    # Recibe y actualiza social_user.extra_data
    'social.pipeline.social_auth.load_extra_data',

    # Actualiza los campos de la instancia user con la información que obtiene vía backend
    'social.pipeline.user.user_details',
)