from __future__ import (
    absolute_import,
)
from django.auth.forms import UserCreationForm
from django.views.generic import (
    CreateView
)
from users.models import UserProfile


class SignUpView(CreateView):

    model = UserProfile
    template_name = 'users/signup.html'
    form_class = UserCreationForm

signup_view = SignUpView.as_view()
