# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [
    path('', views.index, name='home'),
    # página de consulta
    path("consultar-detentores/", views.consulta, name="consulta"),
    path("form-uorg/", views.register_uorg, name="registrar-uorg"),
    path("form-salas/", views.register_sala, name="registrar-salas"),
    path("search/", views.search, name="search"),
    

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

    # Incluir material
    # path('adicionar-material/', views.adicionar_material, name='adicionar_material'),

]
