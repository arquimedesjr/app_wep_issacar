from urllib.request import urlopen

from django.contrib.auth.decorators import login_required
from django.contrib.sites import requests
from django.core.paginator import Paginator
from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404

from ..forms import *
import base64
from io import BytesIO


@login_required
def lista_jovens_presenca(request, tamplate_name="list_jovem.html"):
    query = request.GET.get("campoFilter")
    campoFiltro = FilterJovem()

    if query:
        jovens_presente = Jovens.objects.filter(nome__contains=query)
    else:
        jovens_presente = Jovens.objects.all().order_by('nome')

    paginator = Paginator(jovens_presente, 8)
    page = request.GET.get('page')
    paginacao = paginator.get_page(page)

    if paginacao is not None:
        jovens = {"filtro": campoFiltro, "paginacao": paginacao}
    else:
        jovens = {'lista': jovens_presente, "filtro": campoFiltro}

    if request.method == "POST":
        enviar_relatorio(request)
        return redirect('index')

    return render(request, tamplate_name, jovens)


@login_required
def lista_jovens_nao_presenca(request, tamplate_name="list_jovem_nao.html"):
    query = request.GET.get("campoFilter")
    campoFiltro = FilterJovem()

    if query:
        jovens_presente = JovensNaoPresente.objects.filter(nome__contains=query)
    else:
        jovens_presente = JovensNaoPresente.objects.order_by('id')

    jovens = {'lista': jovens_presente, "filtro": campoFiltro}

    return render(request, tamplate_name, jovens)


@login_required
def enviar_relatorio(request):
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(presenca) from app_jovens WHERE presenca = 'SIM'")
    result = cursor.fetchone()

    cursor.execute("SELECT * FROM app_jovensnaopresente")
    jovensnaopresente = cursor.fetchall()

    if len(jovensnaopresente) is not 0:
        cursor.execute("DELETE FROM app_jovensnaopresente")
        cursor.fetchall()

    cursor.execute("SELECT *  from app_jovens WHERE presenca = 'NÃO'")
    result_jovens_nao = cursor.fetchall()

    print(result_jovens_nao)

    cursor.executemany("INSERT INTO app_jovensnaopresente VALUES(%s, %s, %s, %s, %s,%s, %s, %s)", result_jovens_nao)

    reuniao = request.POST.get("reuniao", None)
    id_reuniao = 2

    if reuniao == 'Algo A +':
        id_reuniao = 1

    if result[0] > 0:
        x = datetime.datetime.now()

    cursor.execute(
        "INSERT INTO app_relatorio "
        "(grupo_id, tribo_id, data, reuniao_id, qnt) "
        "VALUES (%s, %s, %s, %s, %s)",
        [1, 1, x.strftime("%Y") + '-' + x.strftime("%m") + '-' + x.strftime("%d"), id_reuniao, result[0]])

    cursor.execute(
        "UPDATE app_jovens "
        " SET presenca = 'NÃO' WHERE presenca = 'SIM'")


@login_required
def cadastrarJovem(request, template_name='jovem_form.html'):
    if request.method == 'POST':
        form_jovem = JovemForm(request.POST, request.FILES)
        if form_jovem.is_valid():
            form_jovem.save()
            return redirect('lista_jovens')
    else:
        form_jovem = JovemForm()
    return render(request, template_name, {
        'form': form_jovem})


@login_required
def editar_jovem(request, pk, template_name='chamada_form.html'):
    jovem = get_object_or_404(Jovens, pk=pk)
    if request.method == "POST":
        form = EditJovemForm(request.POST, request.FILES, instance=jovem)
        if form.is_valid():
            form.save()
            return redirect('lista_jovens')
    else:
        form = EditJovemForm(instance=jovem)
    return render(request, template_name, {'form': form})


@login_required
def presenca_jovem(request, pk, template_name='chamada_form.html'):
    jovem = get_object_or_404(Jovens, pk=pk)
    if request.method == "POST":
        form = PresencaForm(request.POST, instance=jovem)
        if form.is_valid():
            form.save()
            return redirect('lista_jovens')
    else:
        form = PresencaForm(instance=jovem)
    return render(request, template_name, {'form': form})


@login_required
def delete_jovem(request, pk, template_name='jovem_delete_form.html'):
    jovem = Jovens.objects.get(pk=pk)
    if request.method == "POST":
        jovem.delete()
        return redirect('lista_jovens')
    else:
        form = DeleteJovemForm(instance=jovem)
    return render(request, template_name, {'form': form})


def registrado(request, template_name="registrado.html"):
    return render(request, template_name)
