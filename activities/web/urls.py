from __future__ import (
    absolute_import,
)


from django.conf.urls import (
    include,
    patterns,
    url,
)

from activities.web.views import (
    ActivitiesView,
    AddActivityView,
    DetailActivityView,
    EngageActivityView,
    GalleryView,
)

urlpatterns = patterns(
    '',
    url(r'^add/$', AddActivityView.as_view(), name='add'),
    url(r'^(?P<pk>\d+)/$', DetailActivityView.as_view(), name='detail'),
    url(r'^list/$', ActivitiesView.as_view(), name='list'),
    url(r'^engage/$', EngageActivityView.as_view(), name='engage'),
    url(r'^gallery/$', GalleryView.as_view(), name='gallery'),
)
