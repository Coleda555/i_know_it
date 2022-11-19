from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from users.models import User
from .forms import *



class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')

    class Meta:
        model = User


class SignInView(LoginView):
    template_name = 'registration/login.html'
    form_class = SignInForm
    success_url = reverse_lazy('main')