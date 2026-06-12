from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):

    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Введите логин'
            }
        )
    )

    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Введите пароль'
            }
        )
    )

class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User

        fields = [
            'username',
            'email'
        ]

    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError(
                'Пароли не совпадают'
            )

        return cleaned_data