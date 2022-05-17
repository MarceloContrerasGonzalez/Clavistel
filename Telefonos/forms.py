from  django import forms
from django.forms import ModelForm
from .models import Movil

class TelefonoForm(ModelForm):
    class Meta:
        model = Movil
        fields = ['id_movil','img','costo','descripcion','id_marca','id_tipo_envio']

