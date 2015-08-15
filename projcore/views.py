from django.views.generic.base import View

from projcore.mixins import SiteWideMixin
from organizations.models import Organization

class HomeView(SiteWideMixin, View):

    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(
            *args, **kwargs)
        context['organizations'] = Organization.objects.all().order_by('date_created')[:5]
        return context
