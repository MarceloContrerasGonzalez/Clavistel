from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'Telefonos/index.html')

def login(request):
    return render(request,'Telefonos/login.html')

def consulta(request):
    return render(request,'Telefonos/Nesecitas_Ayuda.html')

def telefonos(request):
    return render(request,'Telefonos/Phones.html')

def registro(request):
    return render(request,'Telefonos/registro.html')