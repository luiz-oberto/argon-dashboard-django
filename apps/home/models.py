# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

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
    nome = models.CharField(max_length=255, null=True, blank=True)
    graduacao = models.CharField(max_length=100, null=True, blank=True)
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

# Modelo Sala (Locais pertencentes a uma UORG)
class Sala(models.Model):
    nome = models.CharField(max_length=50)
    uorg = models.ForeignKey(UORG, on_delete=models.CASCADE, related_name="salas")

    def __str__(self):
        return f"{self.nome} - {self.uorg.codigo}"

# Modelo Item (Itens patrimoniais vinculados a uma UORG e opcionalmente a uma Sala)
class Item(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    numero_patrimonio = models.CharField(max_length=50, unique=True)
    uorg = models.ForeignKey(UORG, on_delete=models.CASCADE, related_name="itens")
    sala = models.ForeignKey(Sala, on_delete=models.SET_NULL, null=True, blank=True, related_name="itens")

    def __str__(self):
        return f"{self.numero_patrimonio} - {self.nome}"
