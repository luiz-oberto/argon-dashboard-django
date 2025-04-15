# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404

# paginator
from django.core.paginator import Paginator
# Q
from django.db.models import Q

# Importando os models
from .models import Detentor,UORG, Sala

# impotando forms
from .forms import UORGForm, SalaForm, ItemForm


# Funções do sistema
def is_admin(user):
    return user.is_staff

def carregar_uorgs(request):
    detentor_id = request.GET.get('detentor_id')
    uorgs = UORG.objects.filter(detentor_id=detentor_id).values('id', 'codigo', 'nome')
    return JsonResponse(list(uorgs), safe=False)

def carregar_salas(request):
    uorg_id = request.GET.get('uorg_id')
    salas = Sala.objects.filter(uorg_id=uorg_id).values('id', 'nome')
    return JsonResponse(list(salas), safe=False)



# página principal
@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


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
    # mostrar Detentores cadastrados
    detentores = Detentor.objects.order_by('nome').prefetch_related('uorgs__salas')

    # paginator
    paginator = Paginator(detentores, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'segment': 'consulta-itens',
        'detentores': detentores,
        'page_obj': page_obj
    }
    
    if request.method == 'GET':
        return render(
            request, 
            'home/consulta-detentores.html', 
            context)


# Administracao de Detentores, UORGs e salas


@user_passes_test(is_admin, login_url='/')
def register_uorg(request):
    msg = None
    success = False
    form = None

    if request.method == "POST":
        form = UORGForm(request.POST)
        if form.is_valid():
            form.save()

            msg = 'UORG criada'
            success = True


        else:
            msg = 'Form is not valid'
    else:
        form = UORGForm()

    return render(request, "home/form-uorg.html", {"form": form, "msg": msg, "success": success, 'segment': 'registrar'})


@user_passes_test(is_admin, login_url='/')
def register_sala(request):
    msg = None
    success = False
    form = None

    if request.method == "POST":
        form = SalaForm(request.POST)
        if form.is_valid():
            form.save()

            msg = 'Sala criada'
            success = True


        else:
            msg = 'Form is not valid'
    else:
        form = SalaForm()

    return render(request, "home/form-salas.html", {"form": form, "msg": msg, "success": success, 'segment': 'registrar'})


# Página Formulário de inclusão de material
@user_passes_test(is_admin, login_url='/')
def register_iten(request):
    msg = None
    success = False
    form = None

    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()

            msg = 'Item criado'
            success = True


        else:
            msg = 'Form is not valid'
    else:
        form = ItemForm()

    return render(request, "home/form-incluir.html", {"form": form, "msg": msg, "success": success, 'segment': 'form-incluir'})


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
