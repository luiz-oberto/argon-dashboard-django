# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class Material(models.Model):
    # Número patrimonial de até 7 dígitos
    numero_patrimonio = models.CharField(
        max_length=7,
        validators=[RegexValidator(regex='^\d{1,7}$', message='Apenas números com até 7 dígitos são permitidos.')]
    )

    # Descrição ou nome do material
    descricao = models.CharField(max_length=255)

    # Preço em reais (com até duas casas decimais)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    # Data de aquisição
    data_aquisicao = models.DateField()

    # Data de inclusão no sistema
    data_inclusao = models.DateField(auto_now_add=True)

    # Status (campo select)
    STATUS_CHOICES = [
        ('novo', 'Novo'),
        ('usado', 'Usado'),
        ('danificado', 'Danificado'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    # Estado do material (campo select)
    ESTADO_CHOICES = [
        ('bom', 'Bom'),
        ('regular', 'Regular'),
        ('ruim', 'Ruim'),
    ]
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)

    # Categoria do produto (campo select)
    CATEGORIA_CHOICES = [
        ('informatica', 'Informática'),
        ('mobilia', 'Mobília'),
        ('outros', 'Outros'),
    ]
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)

    # Origem do Material
    origem = models.TextField()

    # Observação
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.descricao

# novo model para testes
class ItemPatrimonio(models.Model):
    codigo = models.CharField(max_length=7)  # Código de 7 dígitos
    descricao = models.TextField()           # Descrição do item
    local = models.CharField(max_length=100) # Local ou sala, por exemplo

    def __str__(self):
        return self.codigo