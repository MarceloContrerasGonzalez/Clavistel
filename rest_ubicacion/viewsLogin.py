from ast import parse
from urllib import request
from django.shortcuts import render
from rest_framework import status #(codigo de error o exit)
from rest_framework.decorators import api_view #(listar registros)
from rest_framework.response import Response #(dar respuesta)
from rest_framework.parsers import JSONParser #(convertir llos objetos en json)
from django.views.decorators.csrf import csrf_exempt #(seguridad)
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout

@api_view(['POST'])
def login_api(request):

    v_username = request.data['username']
    v_password = request.data['password']
    try:
        usuario = User.objects.get(username = v_username)
    except User.DoesNotExist:
        return render(request, 'Telefonos/inicio_sesion.html')
        
    
    pass_valido = check_password(v_password, usuario.password)
    if not pass_valido:
        return render(request, 'Telefonos/inicio_sesion.html')
    
    token, created = Token.objects.get_or_create(user=usuario)
    login(request, usuario)
    return render(request, 'Telefonos/index.html') 
    #Response(token.key)
