from django.views.generic.base import View

from projcore.mixins import SiteWideMixin

class HomeView(SiteWideMixin, View):

    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(
            *args, **kwargs)
        return context
