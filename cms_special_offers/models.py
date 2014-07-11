#!/bin/env python
# -*- coding: utf-8 -*-
from cms.models import CMSPlugin, Page
from django.db import models
from django.utils.translation import ugettext_lazy as _
from filer.fields.image import FilerImageField
from hvad.models import TranslatableModel, TranslatedFields


class SpecialOffer(TranslatableModel):

    class Meta:
        verbose_name = _(u"cпецпредложение")
        verbose_name_plural = _(u"cпецпредложения")

    translations = TranslatedFields(
        title = models.CharField(
            verbose_name=_(u"заголовок"),
            max_length=256, blank=False, null=True),
        description = models.TextField(
            verbose_name=_(u"описание"),
            blank=True, null=True
        )
    )

    image = FilerImageField(
        verbose_name=_(u"изображение"),
        blank=True, null=True)

    url = models.URLField(blank=True, null=True)
    page_link = models.ForeignKey(
        Page, verbose_name=_(u"страница"), blank=True, null=True,
        on_delete=models.SET_NULL)


    def link(self):
        if self.url:
            link = self.url
        elif self.page_link:
            link = self.page_link.get_absolute_url()
        else:
            link = ""
        return link

    def __unicode__(self):
        return self.title


class SpecialOfferPlugin(CMSPlugin):
    """
    Vehicle vendor selector plugin
    """
