from django.shortcuts import render
from .models import Movil
from .forms import TelefonoForm

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

def agregar_telefono(request):
    datos = {
        'form' : TelefonoForm()
    }
    
    if (request.method == 'POST'):
        formulario = TelefonoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save() #insert a la BD
            datos['mensaje'] = 'Telefono se guardó'
        else:
            datos['mensaje'] = 'Telefono NO se guardó'
  
    return render(request,'Telefonos/agregar_telefono.html', datos)