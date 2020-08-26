from django import forms
from django.forms import ModelForm
from django.views.generic import CreateView

from .models import *


class JovemForm(forms.ModelForm):
    class Meta:
        model = Jovens
        fields = ['foto', 'nome', 'telefone', 'tribo', 'grupo', 'presenca']


class EditJovemForm(forms.ModelForm):
    class Meta:
        model = Jovens
        fields = ['foto', 'nome', 'telefone', 'tribo', 'grupo']


class DeleteJovemForm(forms.ModelForm):
    class Meta:
        model = Jovens
        fields = ['nome']


class PresencaForm(forms.ModelForm):
    class Meta:
        model = Jovens
        fields = ['nome', 'presenca']


class RelatorioForm(forms.ModelForm):
    class Meta:
        model = Relatorio
        fields = ['reuniao']
