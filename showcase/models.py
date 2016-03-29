# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# InBed
# Copyright 2016 Rémy Sanchez <remy.sanchez@hyperthese.net>

from uuid import uuid4
from django.db import models
from uuid_upload_path import upload_to


class Page(models.Model):
    key = models.UUIDField(editable=False, default=uuid4)
    title = models.CharField(max_length=1000)
    background = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


class Design(models.Model):
    page = models.ForeignKey(Page, related_name='designs')
    image = models.ImageField(upload_to=upload_to)
    width = models.IntegerField(editable=False, default=0)
    lateral_margins = models.IntegerField(default=10)

    def __str__(self):
        return '{} {}'.format(self.page.title, self.width)

    def save(self, *args, **kwargs):
        self.width = self.image.width
        return super(Design, self).save(*args, **kwargs)
