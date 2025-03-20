# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404

# paginator
from django.core.paginator import Paginator
# Q
from django.db.models import Q

# página principal
@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


# view de teste
@login_required(login_url="/login/")
def teste_url(request):
    response = 'acessando URL de teste'
    return HttpResponse(response)

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


################## consultar material ###########################

# Página de consultas
@login_required(login_url="/login/")
def consulta(request):
    # mostrar os detentores e seus itens

    # mostrar itens
    itens_patrimonio = ItemPatrimonio.objects.order_by('descricao')

    # paginator
    paginator = Paginator(itens_patrimonio, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'segment': 'consulta-itens',
        'itens': itens_patrimonio,
        'page_obj': page_obj
    }
    
    if request.method == 'GET':
        return render(
            request, 
            'home/consulta-itens.html', 
            context)


# View da barra de pesquisa
def search(request):
    search_value = request.GET.get('q', '').strip()
    # print('search value', search_value)
    if search_value == '':
        return redirect('consulta')

    print(search_value)

    itens_patrimonio = ItemPatrimonio.objects \
        .filter(
            Q(codigo__icontains=search_value) |
            Q(descricao__icontains=search_value) |
            Q(local__icontains=search_value) 
        ) \
        .order_by('descricao')
    
    paginator = Paginator(itens_patrimonio, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    print(itens_patrimonio.query)

    context = {
        'page_obj': page_obj,
        'itens_patrimonio': itens_patrimonio,
        'site_title': 'Itens - ' 
    }

    return render(
        request,
        'home/consulta-itens.html',
        context
    )

# @login_required(login_url="/login/")
# def adicionar_material(request):
#     try:
#         if request.method == 'POST':
#             # Obtém os dados do formulário
#             descricao = request.POST.get('descricao')
#             numero_patrimonio = request.POST.get('numero_patrimonio')
#             preco = request.POST.get('preco')
#             data_aquisicao = request.POST.get('data_aquisicao')
#             status = request.POST.get('status')
#             estado = request.POST.get('estado')
#             categoria = request.POST.get('categoria')
#             origem = request.POST.get('origem')
#             observacao = request.POST.get('observacao')

#             # Cria um novo objeto Material e salva no banco de dados
#             novo_material = Material(
#                 descricao=descricao,
#                 numero_patrimonio=numero_patrimonio,
#                 preco=preco,
#                 data_aquisicao=data_aquisicao,
#                 status=status,
#                 estado=estado,
#                 categoria=categoria,
#                 origem=origem,
#                 observacao=observacao
#             )
#             novo_material.save()

#             return redirect('lista_materiais')
#     except:
#         print('ERRO: Material não incluido')
#         # Redireciona para uma página de sucesso ou lista de materiais

#     # Se for uma requisição GET, apenas renderiza o formulário
#     return render(request, 'form-incluir.html')