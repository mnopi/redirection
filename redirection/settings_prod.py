from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'redirect',
        'USER': 'root',
        'PASSWORD': '1aragon1',
        'HOST': '127.0.0.1',
        'PORT': '3307',
    }
}

ALLOWED_HOSTS = ['igoo.co', '104.236.21.5', 'localhost', '127.0.0.1']
DEBUG = TEMPLATE_DEBUG = False
