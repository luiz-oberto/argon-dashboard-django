# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from . import models

@admin.register(models.Detentor)
class DetentorAdmin(admin.ModelAdmin):
    list_display = 'username',

@admin.register(models.UORG)
class UORGAdmin(admin.ModelAdmin):
    list_display = 'codigo','detentor',

@admin.register(models.Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = 'nome','uorg',

@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = 'numero_patrimonio','nome',


# @admin.register(models.Material)
# class MaterialAdmin(admin.ModelAdmin):
#     list_display = 'numero_patrimonio',
#     'descricao',
#     'preco',
#     'data_aquisicao',
#     'data_inclusao',
#     'estado',
#     'categoria',
#     'origem',
#     'observacao',

# @admin.register(models.ItemPatrimonio)
# class ItemPatrimonioAdmin(admin.ModelAdmin):
#     list_display = 'codigo', 'descricao', 'local',
#     list_per_page = 20

