#!/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from hvad.admin import TranslatableAdmin
from cms_special_offers.models import SpecialOffer
from cms_special_offers.forms import SpecialOfferForm
# Register your models here.


class SpecialOfferAdmin(TranslatableAdmin):
    model = SpecialOffer
    form = SpecialOfferForm

admin.site.register(SpecialOffer, SpecialOfferAdmin)
