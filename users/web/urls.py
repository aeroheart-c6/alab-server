from __future__ import (
    absolute_import,
)
from django.conf.urls import url

from users.web import views

urlpatterns = [
    url(r'^signup/', views.signup_view, name='signup')
]
