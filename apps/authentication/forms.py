# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from apps.home.models import Detentor


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))

# Obs: o nome de cada variável precisa ser igual ao que está em models!!!
class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome completo",
                "class": "form-control"
            }
        ))
    graduacao = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Posto ou Graduação",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))
    is_staff = forms.BooleanField(required=False,
        widget=forms.CheckboxInput(
            attrs={
                "placeholder": "marque se admin",
                "class": "custom-control-input",
                "id": "customCheckRegister",
            }
            )
    )

    class Meta:
        model = Detentor
        fields = ('username', 'email', 'nome', 'graduacao', 'password1', 'password2', 'is_staff')
