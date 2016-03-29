# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# InBed
# Copyright 2016 Rémy Sanchez <remy.sanchez@hyperthese.net>

from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from showcase.views import page

urlpatterns = [
    url(r'^page/(?P<key>[0-9a-f\-]+)', page),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
