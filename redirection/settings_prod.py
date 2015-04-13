from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'redirection',
        'USER': 'root',
        'PASSWORD': '1aragon1',
        'HOST': '127.0.0.1',
        # 'HOST': 'igoo.co',
        'PORT': '3306',
    }
}

ALLOWED_HOSTS = [
    'labelee.com',
    'nupiphone.com',
    'fonopi.com',
    'firstbuy.it',
    'subelamierda.es',
    'subelabasura.es',
    'euride.org',
    'mikios.co',
    'igoo.co',
    '104.131.71.11',
    'localhost',
    '127.0.0.1'
]

DEBUG = TEMPLATE_DEBUG = False
