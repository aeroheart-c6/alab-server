from django.conf.urls import patterns, url
from organizations.web.views import (
    JoinOrganizationView,
    OrganizationProfileFreeView,
    OrganizationProfilePremiumView,
    OrganizationApplicationView,
    PricingView,
)

urlpatterns = patterns('organizations.views',
    url(r'^profile/(?P<id>\d+)/$', OrganizationProfileFreeView.as_view(), name='org_profile_free'),
    url(r'^profile/premium/(?P<id>\d+)/$', OrganizationProfilePremiumView.as_view(), name='org_profile_premium'),
    url(r'^apply/$', OrganizationApplicationView.as_view(), name='org_application'),
    url(r'^join/(?P<id>\d+)/$', JoinOrganizationView.as_view(), name='org_join'),
    url(r'^pricing/$', PricingView.as_view(), name='pricing'),
)
