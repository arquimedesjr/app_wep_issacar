from django import forms
from django.forms import ModelForm
from django.views.generic import CreateView

from .models import *
from input_mask.widgets import InputMask
from django_localflavor_br.forms import BRCPFField, BRPhoneNumberField
from input_mask.contrib.localflavor.br.widgets import BRCPFInput, BRPhoneNumberInput


class DataCustomInput(InputMask):
    mask = {
        'mask': '99/99/9999',
    }


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
