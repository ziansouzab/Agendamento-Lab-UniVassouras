from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django import forms


class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())