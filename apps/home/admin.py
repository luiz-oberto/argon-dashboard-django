# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from . import models

@admin.register(models.Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = 'numero_patrimonio',
    'descricao',
    'preco',
    'data_aquisicao',
    'data_inclusao',
    'estado',
    'categoria',
    'origem',
    'observacao',

@admin.register(models.ItemPatrimonio)
class ItemPatrimonioAdmin(admin.ModelAdmin):
    list_display = 'codigo', 'descricao', 'local',
    list_per_page = 20

