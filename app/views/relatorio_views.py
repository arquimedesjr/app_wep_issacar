from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404

from ..forms import *


@login_required
def lista_relatorio(request, tamplate_name="relatorio.html"):
    jovens_presente = Relatorio.objects.all()
    jovens = {'lista': jovens_presente}

    return render(request, tamplate_name, jovens)


def registrado(request, template_name="registrado.html"):
    return render(request, template_name)
