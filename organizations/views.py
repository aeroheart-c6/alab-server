from django.views.generic.base import View

from organizations.models import (
    Organization
)
from projcore.mixins import SiteWideMixin


class OrganizationProfileFreeView(SiteWideMixin, View):

    template_name = "organizations/profile_free.html"

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
