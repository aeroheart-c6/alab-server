from __future__ import (
    absolute_import,
)
from django.contrib.auth import views as auth_views
from django.conf.urls import (
    include,
    url,
)

from users.web.views import (
    IndexView,
    ProfileEditorView,
    ProfileView,
    SignUpView,
)

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^login/$', auth_views.login, {'template_name':'users/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout_then_login, name='logout'),
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^(?P<username>[\w.@+-]+)/', include([
        url(r'^$', ProfileView.as_view(), name='profile'),
        url(r'^edit/$', ProfileEditorView.as_view(), name='profile_edit'),
    ])),
]
