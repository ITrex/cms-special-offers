#!/bin/env python
# -*- coding: utf-8 -*-
from cms_special_offers.forms import SpecialOfferForm
from cms_special_offers.models import SpecialOffer
from django.contrib import admin
from hvad.admin import TranslatableAdmin


# Register your models here.


class SpecialOfferAdmin(TranslatableAdmin):
    model = SpecialOffer
    form = SpecialOfferForm

admin.site.register(SpecialOffer, SpecialOfferAdmin)
