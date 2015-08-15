from __future__ import (
    absolute_import,
)

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from projcore.views import (
    InstagramRedirectView,
    HomeView,
)

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^complete/instagram/$', InstagramRedirectView.as_view(), name='instagram-callback'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^activity/', include('activities.web.urls', namespace='activities')),
    url(r'^organization/', include('organizations.web.urls', namespace='organizations')),
    url(r'^user/', include('users.web.urls', namespace='users')),

    url(r'^jsreverse/$', 'django_js_reverse.views.urls_js', name='js_reverse'),
    url('', include('social.apps.django_app.urls', namespace='social'))
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT
        })
    ]
