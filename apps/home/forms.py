# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from apps.home.models import UORG, Detentor,Sala


class UORGForm(forms.ModelForm):
    class Meta:
        model = UORG
        fields = ['codigo', 'nome', 'detentor']
        widgets = {
            'codigo': forms.TextInput(attrs={
                "placeholder": "Código",
                "class": "form-control"
            }),
            'nome': forms.TextInput(attrs={
                "placeholder": "Nome da UORG",
                "class": "form-control"
            }),
            'detentor': forms.Select(attrs={
                "class": "form-control"
            }),
        }

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['nome', 'uorg']
        widgets = {
            'nome': forms.TextInput(attrs={
                "placeholder": "Nome da sala",
                "class": "form-control"
            }),
            'uorg': forms.Select(attrs={
                "class": "form-control"
            }),
        }

