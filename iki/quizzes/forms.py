from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea, PasswordInput, EmailInput, CharField, EmailField

from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class AddQuestionForm(ModelForm):
    class Meta:
        model = QuesModel
        fields = '__all__'
