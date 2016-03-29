# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# InBed
# Copyright 2016 Rémy Sanchez <remy.sanchez@hyperthese.net>

from django.contrib import admin
from .models import Page, Design


class DesignInlineAdmin(admin.StackedInline):
    model = Design
    extra = 0
    readonly_fields = ['width']


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ['key']
    inlines = [
        DesignInlineAdmin,
    ]
