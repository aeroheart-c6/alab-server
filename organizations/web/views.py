from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.generic.base import View

from organizations.forms import (
    OrganizationApplicationForm
)
from organizations.models import (
    Organization,
    OrganizationMember,
)
from projcore.mixins import SiteWideMixin


class OrganizationProfileFreeView(SiteWideMixin, View):

    template_name = "organizations/profile-free.html"

    def get_context_data(self, *args, **kwargs):
        context = super(OrganizationProfileFreeView, self).get_context_data(
            *args, **kwargs)

        org_id = self.kwargs.get('id')
        organization = Organization.objects.get(id=int(org_id))
        context['organization'] = organization
        context['id'] = org_id
        context['user'] = self.request.user
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
        context['organization'] = organization
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
        context['application_form'] = OrganizationApplicationForm()
        return context

    def post(self, request, *args, **kwargs):
        application_form = OrganizationApplicationForm(request.POST)
        if application_form.is_valid():
            application_form.save()
            return render(request, 'organizations/application-success.html')
        else:
            return render(request, 'organizations/application.html', {
                'application_form':application_form,
                'error': application_form.errors
            })


class JoinOrganizationView(SiteWideMixin, View):

    def get(self, request, *args, **kwargs):
        context = {}
        organization = Organization.objects.get(id=int(self.kwargs.get('id')))
        user = request.user
        if not organization.is_premium:
            OrganizationMember.objects.create(
                organization=organization,
                user=user,
                is_confirmed=True,
            )
        else:
            OrganizationMember.objects.create(
                organization=organization,
                user=user,
                is_confirmed=False,
            )

        context['message'] = "SUCCESS"

        return JsonResponse(context)
