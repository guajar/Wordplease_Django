from django.contrib.auth import authenticate, login as django_login, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import RedirectView, FormView

from users.forms import LoginForm


class LoginView(FormView):
    form_class = LoginForm
    success_url = reverse_lazy('posts_list')
    template_name = 'login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return self.request.GET.get('next', reverse('posts_list'))


class LogoutView(RedirectView):
    pattern_name = 'login'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)

