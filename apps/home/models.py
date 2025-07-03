# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class DetentorManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O email é obrigatório')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)  # <- Isso define corretamente a senha
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)

class Detentor(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=255, null=False, blank=False, default='new user')
    graduacao = models.CharField(max_length=100, null=False, blank=False, default='new user')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = DetentorManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username



# Modelo UORG (Unidade Organizacional)
class UORG(models.Model):
    codigo = models.CharField(max_length=6, unique=True)  # Código único de 6 dígitos
    nome = models.CharField(max_length=255)
    detentor = models.ForeignKey(Detentor, on_delete=models.CASCADE, related_name="uorgs")

    def __str__(self):
        return f"{self.codigo} - {self.nome}"

# CRIAR MODELO BLOCO
class Bloco(models.Model):
    BLOCO_CHOICES = [
        ('BLOCO A', 'Bloco A'),
        ('BLOCO B', 'Bloco B'),
        ('BLOCO C', 'Bloco C'),
        ('BLOCO D', 'Bloco D'),
        ('BLOCO E', 'Bloco E'),
        ('BLOCO F', 'Bloco F'),
        ('BLOCO G', 'Bloco G'),
        ('BLOCO H', 'Bloco H'),
        ('BLOCO I', 'Bloco I'),
        ('BLOCO J', 'Bloco J'),
        ('BLOCO K', 'Bloco K'),
        ('BLOCO L', 'Bloco L'),
        ('BLOCO M', 'Bloco M'),
        ('BLOCO N', 'Bloco N'),
        ('BLOCO O', 'Bloco O'),
        ('BLOCO P', 'Bloco P'),
        ('BLOCO Q1', 'Bloco Q1'), 
        ('BLOCO Q2', 'Bloco Q2'), 
        ('BLOCO T', 'Bloco T'),
    ]

    nome = models.CharField(max_length=20, choices=BLOCO_CHOICES, unique=True)

    def __str__(self):
        return self.nome

# Modelo Sala (Locais pertencentes a uma UORG)
class Sala(models.Model):
    nome = models.CharField(max_length=50)
    uorg = models.ForeignKey(UORG, on_delete=models.CASCADE, related_name="salas")
    bloco = models.ForeignKey(Bloco, on_delete=models.CASCADE, related_name="salas")

    def __str__(self):
        return f"{self.nome} - {self.uorg.codigo} - {self.bloco.nome}"

# Modelo Item (Itens patrimoniais vinculados a uma UORG e opcionalmente a uma Sala)
class Item(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    numero_patrimonio = models.CharField(max_length=50, unique=True)
    uorg = models.ForeignKey(UORG, on_delete=models.CASCADE, related_name="itens")
    sala = models.ForeignKey(Sala, on_delete=models.SET_NULL, null=True, blank=True, related_name="itens")

    def __str__(self):
        return f"{self.numero_patrimonio} - {self.nome}"

# transferencia
class Transferencia(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('autorizada', 'Autorizada'),
        ('recusada', 'Recusada'),
        ('cancelada', 'Cancelada'),
    ]
    detentor_origem = models.ForeignKey(
        'Detentor', on_delete=models.PROTECT, related_name='transferencias_origem'
    )
    detentor_destino = models.ForeignKey(
        'Detentor', on_delete=models.PROTECT, related_name='transferencias_destino'
    )
    gerente = models.ForeignKey(
        'Detentor', on_delete=models.PROTECT, related_name='transferencias_gerente'
    )
    uorg_origem = models.ForeignKey(
        'UORG', on_delete=models.PROTECT, related_name='transferencias_uorg_origem'
    )
    uorg_destino = models.ForeignKey(
        'UORG', on_delete=models.PROTECT, related_name='transferencias_uorg_destino'
    )
    sala_origem = models.ForeignKey(
        'Sala', on_delete=models.PROTECT, related_name='transferencias_sala_origem', null=True, blank=True
    )
    sala_destino = models.ForeignKey(
        'Sala', on_delete=models.PROTECT, related_name='transferencias_sala_destino', null=True, blank=True
    )
    status_transferencia = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pendente'
    )
    obs = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    data_aprovacao = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'Transferência #{self.id} - {self.get_status_transferencia_display()}'

class TransferenciaItem(models.Model):
    transferencia = models.ForeignKey(
        'Transferencia', on_delete=models.CASCADE, related_name='itens'
    )
    item = models.ForeignKey('Item', on_delete=models.PROTECT, related_name='itens_transferidos')

    def __str__(self):
        return f'{self.item} (Transf. {self.transferencia.id})'

