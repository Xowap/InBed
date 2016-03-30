# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# InBed
# Copyright 2016 Rémy Sanchez <remy.sanchez@hyperthese.net>

# noinspection PyUnresolvedReferences
from .base import *
from os import getenv

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = getenv('AWS_S3_CUSTOM_DOMAIN')
AWS_S3_URL_PROTOCOL = 'https:'

AWS_HEADERS = {
    'Expires': 'Thu, 1 Jan 2030 20:00:00 GMT',
    'Cache-Control': 'max-age=315360000',
}

ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
