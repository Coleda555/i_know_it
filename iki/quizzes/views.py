from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views.generic import ListView

from .forms import *
from .models import *
from django.http import HttpResponse


# Create your views here.
class ContextMixin:

    context = {
        'site_title': 'VeryCoolNewsPortal',
        'facebook': 'https://facebook.com',
        'twitter': 'https://twitter.com',
        'github': 'https://github.com',
    }


class QuesView(ContextMixin, ListView):
    model = QuesModel
    template_name = 'quizzes/index.html'
    context_object_name = 'question'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(QuesView, self).get_context_data()
        context.update(self.context)
        context['user'] = self.request.user
        return context