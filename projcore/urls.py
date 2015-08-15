from __future__ import (
    absolute_import,
)

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^activity/', include('activities.web.urls', namespace='activities')),
    url(r'^organization/', include('organizations.urls', namespace='organizations')),
    url(r'^users/', include('users.web.urls', namespace='users')),

]
