# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from apps.home.models import Detentor, UORG, Sala, Item

# Formulário para inclusão de detentores, UORGs e salas
class UORGForm(forms.ModelForm):
    detentor = forms.ModelChoiceField(
        queryset=Detentor.objects.all(),
        required=True,
        empty_label="Detentor",
        widget=forms.Select(attrs={"class": "form-control"})
    )
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
        }

class SalaForm(forms.ModelForm):
    uorg = forms.ModelChoiceField(
        queryset=UORG.objects.all(),
        required=True,
        empty_label="Selecine a UORG",
        widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = Sala
        fields = ['nome', 'uorg']
        widgets = {
            'nome': forms.TextInput(attrs={
                "placeholder": "Nome da sala",
                "class": "form-control"
            }),
        }

# formulário para inclusão de material
class ItemForm(forms.ModelForm):
    detentor = forms.ModelChoiceField(
        queryset=Detentor.objects.all(),
        required=False,
        empty_label= "Detentor",
        widget=forms.Select(attrs={"class": "form-control"})
    )

    uorg = forms.ModelChoiceField(
        queryset=UORG.objects.all(),
        required=False,
        empty_label='UORG',
        widget=forms.Select(attrs={"class": "form-control"})
    )

    sala = forms.ModelChoiceField(
        queryset=Sala.objects.all(),
        required=False,
        empty_label="Sala",
        widget=forms.Select(attrs={"class":"form-control"})
    )
    class Meta:
        model = Item
        fields = ['detentor', 'uorg', 'sala', 'nome', 'descricao', 'numero_patrimonio']
        widgets = {
            'nome': forms.TextInput(attrs={
                "placeholder": "Nome do item",
                "class": "form-control"
            }),
            'descricao': forms.TextInput(attrs={
                "placeholder": "Descrição do item",
                "class": "form-control"
            }),
            'numero_patrimonio': forms.NumberInput(attrs={
                "placeholder": "Número patrimonial",
                "class": "form-control"
            }),
        }

    def clean_numero_patrimonio(self):
        numero = self.cleaned_data['numero_patrimonio']
        if not numero.isdigit():
            raise forms.ValidationError("Digite apenas números.")
        return numero