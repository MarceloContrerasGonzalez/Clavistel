from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'Telefonos/index.html')

def login(request):
    return render(request,'login/login.html')

def consulta(request):
    return render(request,'consulta/Nesecitas_Ayuda.html')

def telefonos(request):
    return render(request,'Telefonos/Phones.html')

def registro(request):
    return render(request,'registro/registro.html')