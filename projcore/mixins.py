from __future__ import (
    absolute_import,
)

from django.views.generic.base import TemplateResponseMixin


class SiteWideMixin(TemplateResponseMixin):
    """
    A mixin that will have context data or other functions to 
    be used sitewide.
    """
    editable_content = None

    def __init__(self):
        user = None

    def get_context_data(self, **context):
        return context

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())
