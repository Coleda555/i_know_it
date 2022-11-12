from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import CharField, TextInput, PasswordInput, EmailInput, EmailField


class RegistrationForm(UserCreationForm):
    firstname = CharField(
        widget=TextInput(
            attrs={
                'name': 'first_name',
                'id': 'first_name',
                'placeholder': 'Введите ваше имя'
            }
        )
    )
    lastname = CharField(
        widget=TextInput(
            attrs={
                'name': 'last_name',
                'id': 'last_name',
                'placeholder': 'Введите вашу фамилию'
            }
        )
    )
    password1 = CharField(
        widget=PasswordInput(
            attrs={
                'name': 'pass',
                'id': 'pass',
                'placeholder': 'Введите пароль'
            }
        )
    )
    password2 = CharField(
        widget=PasswordInput(
            attrs={
                'name': 're_pass',
                'id': 're_pass',
                'placeholder': 'Повторите ваш пароль'
            }
        )
    )
    email = EmailField(
        widget=EmailInput(
            attrs={
                'name': 'email',
                'id': 'email',
                'placeholder': 'Введите ваш Email'
            }
        )
    )


class SignInForm(AuthenticationForm):
    username = EmailField(
        widget=EmailInput(
            attrs={
                'name': 'your_email',
                'id': 'your_email',
                'placeholder': 'E-mail'
            }
        )
    )
    password = CharField(
        widget=PasswordInput(
            attrs={
                'name': 'your_pass',
                'id': 'your_pass',
                'placeholder': 'Password'
            }
        )
    )
