from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404

from ..forms import *


@login_required
def lista_jovens_presenca(request, tamplate_name="list_jovem.html"):
    jovens_presente = Jovens.objects.all()
    jovens = {'lista': jovens_presente}

    if request.method == "POST":
        enviar_relatorio(request)
        return redirect('index')

    return render(request, tamplate_name, jovens)


def enviar_relatorio(request):
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(presenca) from app_jovens WHERE presenca = 'SIM'")
    result = cursor.fetchone()
    print(result)

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
        (1, 1, x.strftime("%Y") + '-' + x.strftime("%m") + '-' + x.strftime("%d"), id_reuniao, result))


@login_required
def cadastrarJovem(request, template_name='jovem_form.html'):
    if request.method == 'POST':
        form_jovem = JovemForm(request.POST, request.FILES)
        print(form_jovem)
        if form_jovem.is_valid():
            form_jovem.save()
            return redirect('lista_jovens')
    else:
        form_jovem = JovemForm()
    return render(request, template_name, {
        'form': form_jovem})


def editar_jovem(request, pk, template_name='chamada_form.html'):
    jovem = get_object_or_404(Jovens, pk=pk)
    if request.method == "POST":
        form = EditJovemForm(request.POST, instance=jovem)
        if form.is_valid():
            form.save()
            return redirect('lista_jovens')
    else:
        form = EditJovemForm(instance=jovem)
    return render(request, template_name, {'form': form})


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
