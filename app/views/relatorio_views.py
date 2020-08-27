from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ..forms import *


@login_required
def lista_relatorio(request, tamplate_name="relatorio.html"):
    jovens_presente = Relatorio.objects.all()
    jovens = {'lista': jovens_presente}

    return render(request, tamplate_name, jovens)


def registrado(request, template_name="registrado.html"):
    return render(request, template_name)
