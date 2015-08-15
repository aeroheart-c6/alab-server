from __future__ import (
    absolute_import,
)

import httplib

from django.http import (
    HttpResponse,
    JsonResponse,
)
from django.utils.translation import ugettext as _
from django.views.generic.base import (
    TemplateView,
    View,
)

from activities.models import (
    Activity,
    ActivityParticipant
)
from activities.forms import ActivityForm


class AddActivityView(TemplateView):

    """
    """

    template_name = 'activities/add_form.html'

    def get(self, *args, **kwargs):
        context = self.get_context_data()
        context['form'] = ActivityForm()

        return self.render_to_response(context)

    def post(self, *args, **kwargs):
        context = {}
        form = ActivityForm(self.request.POST)

        if form.is_valid():
            form.save(commit=True)

        context['form'] = form

        return self.render_to_response(context)


class ActivitiesView(TemplateView):

    """
    """

    template_name = 'activities/list.html'

    def get(self, *args, **kwargs):
        context = self.get_context_data()
        engaged_activities = ActivityParticipant.objects.filter(user=self.request.user).values_list('activity')
        context['activities'] = Activity.objects.exclude(id__in=engaged_activities)

        return self.render_to_response(context)


class EngageActivityView(View):

    """
    """

    def get(self, request, *args, **kwargs):
        context = {}
        activity = Activity.objects.get(slug=self.request.GET.get('slug'))
        participant = self.request.user

        obj, created = ActivityParticipant.objects.get_or_create(
            activity=activity,
            user=participant,
        )

        context['message'] = "SUCCESS"

        return JsonResponse(context)


class GalleryView(View):
    """
    """
    def get(self, request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponse(_('Invalid request'), status=httplib.BAD_REQUEST)
        
        user = request.user
        
        if not user.is_authenticated():
            return JsonResponse({'message': _('Unauthorized')}, status=httplib.UNAUTHORIZED)
        
        if not user.profile.instagram_token:
            return JsonResponse({'message': _('Access Token Required')}, status=httplib.FORBIDDEN)
        
        return JsonResponse([
            
        ])
