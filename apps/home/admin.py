# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from . import models

@admin.register(models.Detentor)
class DetentorAdmin(admin.ModelAdmin):
    list_display = "id",'username', 'is_active', 'is_staff', 

@admin.register(models.UORG)
class UORGAdmin(admin.ModelAdmin):
    list_display = 'codigo','nome','detentor',

@admin.register(models.Bloco)
class BlocoAdmin(admin.ModelAdmin):
    list_display = 'nome',

@admin.register(models.Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = 'nome','uorg', 'bloco',

@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = 'numero_patrimonio','nome', 'uorg', 'sala',

@admin.register(models.Transferencia)
class TransferenciaAdmin(admin.ModelAdmin):
    list_display = 'detentor_origem','detentor_destino', 'gerente', 'uorg_origem', 'uorg_destino', 'sala_origem', 'sala_destino', 'status_transferencia',
