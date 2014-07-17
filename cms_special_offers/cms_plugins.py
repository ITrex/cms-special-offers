#!/bin/env python
# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms_special_offers.models import (
    SpecialOfferPlugin, SpecialOffer)
from django.utils.translation import ugettext as _


class CMSSpecialOfferPlugin(CMSPluginBase):
    model = SpecialOfferPlugin
    name = _(u"Спецпредложения")
    render_template = "cms_special_offers/special_offer_plugin.html"


    def render(self, context, instance, placeholder):
        context.update({'instance': instance,
                        'object_list': SpecialOffer.objects.all()})

        return context

plugin_pool.register_plugin(CMSSpecialOfferPlugin)
