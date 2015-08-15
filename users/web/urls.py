from __future__ import (
    absolute_import,
)
from django.conf.urls import url

from users.web import views

urlpatterns = [
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^signup/', views.signup_view, name='signup'),
    url(r'^', views.index_view, name='index')
]
