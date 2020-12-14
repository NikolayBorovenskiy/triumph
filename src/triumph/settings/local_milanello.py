# coding: utf-8

import socket
import typing

from triumph.settings.base import *

DEBUG = True

INTERNAL_IPS = ['127.0.0.1', '10.0.2.2']


def define_internal_docker_ips(ips_range: int = 20) -> typing.Generator:
    """Only docker specific"""
    _, _, ips = socket.gethostbyname_ex(socket.gethostname())
    for ip in ips:
        for i in range(ips_range):
            yield ip[:-1] + str(i)


if DEBUG:
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
    LOGGING['loggers'][''] = {
        'handlers': ['stdout'],
        'level': 'DEBUG',
    }
    possible_docker_ips = list(define_internal_docker_ips())
    INTERNAL_IPS.extend(possible_docker_ips)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/tmp/django_cache_triumph',
    }
}

ADMINS = (('Nikolay', 'nikolay.borovenskiy@gmail.com'),)
DEFAULT_ADMIN_PASSWORD = 'admin'

ALLOWED_HOSTS = ['*', ]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
