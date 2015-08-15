from django.shortcuts import redirect
from django.views.generic.base import View

from organizations.models import (
    Organization
)
from projcore.mixins import SiteWideMixin


class OrganizationProfileFreeView(SiteWideMixin, View):

    template_name = "organizations/profile-free.html"

    def get_context_data(self, *args, **kwargs):
        context = super(OrganizationProfileFreeView, self).get_context_data(
            *args, **kwargs)

        org_id = self.kwargs.get('id')
        organization = Organization.objects.get(id=int(org_id))
        context['name'] = organization.name
        context['address'] = organization.address
        context['city'] = organization.city
        context['country'] = organization.country
        return context


class OrganizationProfilePremiumView(SiteWideMixin, View):

    template_name = "organizations/profile-premium.html"

    def get_context_data(self, *args, **kwargs):
        context = super(OrganizationProfilePremiumView, self).get_context_data(
            *args, **kwargs)
        org_id = self.kwargs.get('id')
        organization = Organization.objects.get(id=int(org_id))
        context['name'] = organization.name
        context['address'] = organization.address
        context['city'] = organization.city
        context['country'] = organization.country
        return context

    def get(self, request, *args, **kwargs):
        org_id = self.kwargs.get('id')
        organization = Organization.objects.get(id=int(org_id))
        if not organization.is_premium:
            return redirect('organizations:org_profile_free', id=org_id)
        return self.render_to_response(self.get_context_data())

class OrganizationApplicationView(SiteWideMixin, View):

    template_name = "organizations/application.html"

    def get_context_data(self, *args, **kwargs):
        context = super(OrganizationApplicationView, self).get_context_data(
            *args, **kwargs)
