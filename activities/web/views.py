from __future__ import (
    absolute_import,
)


from django.views.generic.base import TemplateView

from activities.models import Activity
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
