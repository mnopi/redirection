from .settings import *
import settings


settings.DATABASES['default']['PASSWORD'] = '1aragon1'

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
    'phasion.co',
    'localhost',
    '127.0.0.1',
]
ALLOWED_HOSTS += DOMAINS_JOSKO
ALLOWED_HOSTS += DOMAINS_YERAY
ALLOWED_HOSTS += DOMAINS_RAMON

DEBUG = TEMPLATE_DEBUG = False
