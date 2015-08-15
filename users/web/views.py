from __future__ import (
    absolute_import,
)
from django.contrib.auth import (
    authenticate,
    login
)
from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponseRedirect
from django.views.generic import (
    FormView,
    TemplateView
)

from cities_light.models import City, Country
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
        context['cities'] = City.objects.all()
        context['countries'] = Country.objects.all()
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
                username=user_form.data.get('username'),
                password=user_form.data.get('password1')
            )
            login(self.request, user)
            return HttpResponseRedirect(self.success_url)
        else:
            context = {}
            context['user_form'] = user_form
            context['user_profile_form'] = user_profile_form
            context['cities'] = City.objects.all()
            context['countries'] = Country.objects.all()
            return self.render_to_response(context)
signup_view = SignUpView.as_view()


class IndexView(TemplateView):

    template_name = 'users/index.html'

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse_lazy('home'))

index_view = IndexView.as_view()
