from __future__ import (
    absolute_import,
)


from django.conf.urls import (
    include,
    patterns,
    url,
)

from activities.web.views import (
    AddActivityView,
)

urlpatterns = patterns(
    '',
    url(r'^add/$', AddActivityView.as_view(), name='add'),
)
