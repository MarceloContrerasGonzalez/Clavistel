from  django import forms
from django.forms import ModelForm
from .models import Movil, Sucursal
from django.contrib.auth .forms import UserCreationForm
from django.contrib.auth.models import User

class TelefonoForm(ModelForm):
    class Meta:
        model = Movil
        fields = ['id_movil','nombre','img','costo','marca','tipo_envio']
        
class SucursalForm(ModelForm):
    class Meta:
        model = Sucursal
        fields = ['id_sucursal','nombre_sucursal','direccion','region']
        
''' REGISTRO '''

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=250, help_text='Requiered. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'email','password1', 'password2', 'is_staff')