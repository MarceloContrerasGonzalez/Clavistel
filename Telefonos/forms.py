from  django import forms
from django.forms import ModelForm
from .models import Movil

class TelefonoForm(ModelForm):
    class Meta:
        model = Movil
        fields = ['id_movil','nombre','img','costo','marca','tipo_envio']

