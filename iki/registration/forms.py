from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import CharField, TextInput, PasswordInput, EmailInput, EmailField


class RegistrationForm(UserCreationForm):
    firstname = CharField(
        widget=TextInput(
            attrs={
                'name': 'name',
                'id': 'name',
                'class': 'kb_oof1',
                'type': 'text',
                'maxlength': '30',
                'placeholder': 'Имя',
                'required': True

            }
        )
    )
    lastname = CharField(
        widget=TextInput(
            attrs={
                'name': 'lastname',
                'id': 'lastname',
                'class': 'kb_oof1',
                'type': 'text',
                'maxlength': '30',
                'placeholder': 'Фамилия',
                'required': True
            }
        )
    )
    password1 = CharField(
        widget=PasswordInput(
            attrs={
                'name': 'new_pass',
                'id': 'new_pass',
                'class': 'kb_oof1',
                'type': 'password',
                'maxlength': '30',
                'placeholder': 'Введите пароль',
                'required': True

            }
        )
    )
    password2 = CharField(
        widget=PasswordInput(
            attrs={
                'name': 'new_pass2',
                'id': 'new_pass2',
                'class': 'kb_oof1',
                'type': 'password',
                'maxlength': '30',
                'placeholder': 'Повторите ваш пароль',
                'required': True
            }
        )
    )
    email = EmailField(
        widget=EmailInput(
            attrs={
                'name': 'email',
                'id': 'email',
                'class': 'kb_oof1',
                'type': 'email',
                'maxlength': '30',
                'placeholder': 'E-mail',
                'required': True

            }
        )
    )


class SignInForm(AuthenticationForm):
    username = CharField(
        widget=TextInput(
            attrs={
                'name': 'your_name',
                'id': 'your_name',
                'placeholder': 'Имя'
            }
        )
    )
    password = CharField(
        widget=PasswordInput(
            attrs={
                'name': 'your_pass',
                'id': 'your_pass',
                'placeholder': 'Пароль'
            }
        )
    )
