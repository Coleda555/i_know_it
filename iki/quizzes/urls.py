from django.urls import path

from .views import *


urlpatterns = [
    path('', QuesView.as_view(), name='main'),
    # path('addQuestion/', addQuestion, name='addquestion'),

]