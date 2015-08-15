from __future__ import (
    absolute_import,
)

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^organization/', include('organizations.urls', namespace='organizations')),
]
