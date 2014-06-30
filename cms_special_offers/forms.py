#!/bin/env python
# -*- coding: utf-8 -*-

from hvad.forms import TranslatableModelForm
from django.utils.translation import ugettext_lazy as _
from cms_special_offers.models import SpecialOffer
from cms.models import Page
from django.forms.widgets import Media
from cms.forms.fields import PageSelectFormField


class SpecialOfferForm(TranslatableModelForm):
    page_link = PageSelectFormField(
        queryset=Page.objects.drafts(),
        label=_(u"страница"), required=False)
