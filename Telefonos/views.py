from django.shortcuts import render
from .models import Movil

# Create your views here.
def home(request):
    return render(request,'Telefonos/index.html')

def login(request):
    return render(request,'login/login.html')

def consulta(request):
    return render(request,'consulta/Nesecitas_Ayuda.html')

def telefonos(request):
    lista_Movil = Movil.objects.all()
    datos = {
        'lista_Movil' : lista_Movil
    }
    return render(request,'Telefonos/Phones.html', datos)

def registro(request):
    return render(request,'registro/registro.html')