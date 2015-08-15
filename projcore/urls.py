from __future__ import (
    absolute_import,
)

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from projcore.views import HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^activity/', include('activities.web.urls', namespace='activities')),
    url(r'^organization/', include('organizations.web.urls', namespace='organizations')),
    url(r'^users/', include('users.web.urls', namespace='users')),

    url(r'^jsreverse/$', 'django_js_reverse.views.urls_js', name='js_reverse'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT
        })
    ]
