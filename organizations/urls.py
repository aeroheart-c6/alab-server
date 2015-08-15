from django.conf.urls import patterns, url
from organizations.views import (
    OrganizationProfileFreeView
)

urlpatterns = patterns('organizations.views',
    url(r'^profile/(?P<id>\d+)/$', OrganizationProfileFreeView.as_view(), name='org_profile_free'),
)
