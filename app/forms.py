from django import forms
from django.forms import ModelForm
from django.views.generic import CreateView

from .models import *


class JovemForm(forms.ModelForm):
    class Meta:
        model = Jovens
        fields = ['foto', 'nome', 'telefone', 'tribo', 'grupo', 'presenca']


class JovemBase64(forms.ModelForm):
    class Meta:
        model = Jovens
        fields = ['foto_base64']


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


class FilterJovem(forms.Form):
    campoFilter = forms.CharField(label=False, max_length=100)
    campoFilter.widget.attrs.update({'class': 'form-control', 'placeholder': 'Pesquisar Jovem'})
