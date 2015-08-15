from __future__ import (
    absolute_import,
)
from django.contrib.auth import (
    authenticate,
    login,
    logout as auth_logout
)
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse, reverse_lazy
from django.http.response import HttpResponseRedirect
from django.views.generic import (
    FormView,
    TemplateView,
    RedirectView
)

from users.forms import UserForm, SignUpProfileForm
from users.models import UserProfile


class SignUpView(FormView):

    template_name = 'users/signup.html'
    form_class = UserForm
    success_url = reverse_lazy('users:index')

    def get_context_data(self, *args, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        context['user_form'] = UserForm
        context['user_profile_form'] = SignUpProfileForm
        return context

    def post(self, request, *args, **kwargs):
        user_form = UserForm(request.POST)
        user_profile_form = SignUpProfileForm(request.POST)
        if user_form.is_valid() and user_profile_form.is_valid():
            user = user_form.save()
            user_profile = UserProfile(
                user = user,
                city = user_profile_form.data['city'],
                country = user_profile_form.data['country']
            )
            user_profile.save()
            user = authenticate(
                username=self.request.POST['username'],
                password=self.request.POST['password']
            )
            login(self.request, user)
            return HttpResponseRedirect(self.success_url)
        else:
            context = {}
            context['user_form'] = user_form
            context['user_profile_form'] = user_profile_form
            return self.render_to_response(context)
signup_view = SignUpView.as_view()


class LoginView(FormView):

    success_url = reverse_lazy('users:index')
    form_class = AuthenticationForm
    template_name = 'users/login.html'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)
login_view = LoginView.as_view()


class LogoutView(RedirectView):

    def get_redirect_url(self):
        auth_logout(self.request)
        return reverse('users:index')
logout_view = LogoutView.as_view()

class IndexView(TemplateView):

    template_name = 'users/index.html'
index_view = IndexView.as_view()
