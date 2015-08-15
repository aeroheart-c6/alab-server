from __future__ import (
    absolute_import,
)


from django.http import JsonResponse
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
        # engaged_activities = ActivityParticipant.objects.filter(user=self.request.user).values_list('id')
        # context['activities'] = Activity.objects.exclude()
        context['activities'] = Activity.objects.all()

        return self.render_to_response(context)


class EngageActivityView(View):

    """
    """

    def get(self, *args, **kwargs):
        context = {}
        activity = Activity.objects.get(slug=self.request.GET.get('slug'))
        participant = self.request.user

        obj, created = ActivityParticipant.objects.get_or_create(
            activity=activity,
            user=participant,
        )

        context['message'] = "SUCCESS"

        return JsonResponse(context)
