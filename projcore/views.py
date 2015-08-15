from __future__ import (
    absolute_import,
)

from django.http import HttpResponse
from django.views.generic.base import View

from organizations.models import Organization
from projcore.mixins import SiteWideMixin


class HomeView(SiteWideMixin, View):

    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(
            *args, **kwargs)
        context['organizations'] = Organization.objects.all().order_by('date_created')[:5]
        return context


class InstagramRedirectView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse()
