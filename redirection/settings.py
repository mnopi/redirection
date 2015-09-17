# -*- coding: utf-8 -*-

"""
Django settings for redirection project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&qd4c$z0xl#h)7(040-v0$n13us3e7$jhikl3u3^zqhj%z_(c$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'redirect',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (

    # Put your context processors here
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    "django.core.context_processors.media",
)

ROOT_URLCONF = 'redirection.urls'

WSGI_APPLICATION = 'redirection.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

CONNECTION_NAME_JOSKO = 'twitterbots_josko'
CONNECTION_NAME_YERAY = 'twitterbots_yeray'
CONNECTION_NAME_RAMON = 'twitterbots_ramon'
DATABASE_NAME_JOSKO = 'twitter_bots_prod'
DATABASE_NAME_YERAY = 'twitter_bots_prod'
DATABASE_NAME_RAMON = 'twitter_bots_dev_ramon'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sync_pagelinks',
        "USER": "root",
        "PASSWORD": "1aragon1",
        "HOST": "127.0.0.1",
    },
    CONNECTION_NAME_JOSKO: {
        'NAME': DATABASE_NAME_JOSKO,
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': '1aragon1',
        'HOST': '46.101.61.145',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
    },
    CONNECTION_NAME_YERAY: {
        'NAME': DATABASE_NAME_YERAY,
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': '1aragon1',
        'HOST': '46.101.61.145',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
    },
    CONNECTION_NAME_RAMON: {
        'NAME': DATABASE_NAME_RAMON,
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': '1aragon1',
        'HOST': '46.101.61.145',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}

# esto no es necesario puesto que hacemos .using(connection_to_use) para hacer un quertyset sobre una conexión específica
# DATABASE_ROUTERS = (
#     'redirect.twitter_bots_router.TwitterBotsRamonRouter',
#     'redirect.twitter_bots_router.TwitterBotsYerayRouter',
#     'redirect.twitter_bots_router.TwitterBotsJoscoRouter',
# )


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'debug.log'),
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

APPEND_SLASH = True


# Lista de dominios para cada uno

DOMAINS_JOSKO = [
    'bogadgam.biz',
    'gameias.biz',
    'bogaia.biz',
    'jueggam.biz',
    'geniglam.biz',
    'fashiglam.biz',
    'phasglam.biz',
    'phanio.biz',
    'genigam.biz',
    'bogaglam.biz',
    'bogaes.biz',
    'bogadias.biz',
    'bogadglam.biz',
    'phasgam.biz',
    'phanios.biz',
    'phanin.biz',
    'modagam.biz',
    'juegias.biz',
    'juegia.biz',
    'jueges.biz',
]
DOMAINS_YERAY = [
    'realplaying.info'
    'demongamer.info'
    'gamersbulk.info'
    'gamewebber.info'
    'prossimoda.info'
    'esforfresh.info'
    'estilomanos.info'
    'chicpose.info',
]
DOMAINS_RAMON = [
    'divhana.info',
    'femmsacion.info',
    'modentidad.info',
    'comunamoda.info',
    'divinias.info',
    'cleanandplay.info',
    'relaxinggame.info',
    'happiergaming.info',
    'gameforblame.info',
    'blameforgame.info',
    'gameinthepain.info',
]


#
# Aquí ponemos a qué base de datos se tiene que conectar con cada dominio
DOMAINS_IDX_BY_CONNECTION = {
    CONNECTION_NAME_JOSKO: DOMAINS_JOSKO,
    CONNECTION_NAME_YERAY: DOMAINS_YERAY,
    CONNECTION_NAME_RAMON: DOMAINS_RAMON,
}