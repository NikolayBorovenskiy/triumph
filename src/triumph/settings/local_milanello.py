# coding: utf-8

import dj_database_url

from triumph.settings.base import *

DEBUG = True

if DEBUG:
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'triumph',
        'USER': 'triumphuser',
        'PASSWORD': 'acmilan86',
        'HOST': 'localhost',
        'PORT': '',
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/tmp/django_cache_triumph',
    }
}

ALLOWED_HOSTS = ['*', ]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INTERNAL_IPS = ['127.0.0.1']
