from __future__ import (
    absolute_import,
)
from django.contrib.auth import views as auth_views
from django.conf.urls import url

from users.web import views

urlpatterns = [
    url(r'^login/', auth_views.login, {'template_name':'users/login.html'}, name='login'),
    url(r'^logout/', auth_views.logout_then_login, name='logout'),
    url(r'^signup/', views.signup_view, name='signup'),
    url(r'^', views.index_view, name='index')
]
