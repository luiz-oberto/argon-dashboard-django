# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from . import models

@admin.register(models.Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = 'descricao',
    'numero_patrimonio',
    'preco',
    'data_aquisicao',
    'data_inclusao',
    'estado',
    'categoria',
    'origem',
    'observacao',
