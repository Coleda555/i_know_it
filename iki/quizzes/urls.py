from django.urls import path

from .views import *


urlpatterns = [
    path('', QuesView.as_view(), name='main'),
    path('wall_user', WallUserView.as_view(), name='wall_user'),
    # path('addQuestion/', addQuestion, name='addquestion'),

]