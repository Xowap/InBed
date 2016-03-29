# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# InBed
# Copyright 2016 Rémy Sanchez <remy.sanchez@hyperthese.net>

from django.db.models import F, Min
from django.shortcuts import get_object_or_404, render
from django.db.models.functions import Value as V

from .models import Page


def page(request, key):
    page = get_object_or_404(Page, key=key)

    qs = (page.designs
          .order_by('width')
          .annotate(min_width=F('width') + F('lateral_margins') * V(2)))

    return render(request, 'showcase.html', {
        'page': page,
        'min_width': qs.aggregate(w=Min('min_width'))['w'],
        'designs': list(qs),
    })
