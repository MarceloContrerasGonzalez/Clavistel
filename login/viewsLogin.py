from ast import parse
import re
from django.shortcuts import render
from rest_framework import status #(codigo de error o exit)
from rest_framework.decorators import api_view #(listar registros)
from rest_framework.response import Response #(dar respuesta)
from rest_framework.parsers import JSONParser #(convertir llos objetos en json)
from django.views.decorators.csrf import csrf_exempt #(seguridad)
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)
    v_username = data['username']
    v_password = data['password']
    try:
        usuario = User.objects.get(username = v_username)
    except User.DoesNotExist:
        return Response("Usuario Invalido")
    
    pass_valido = check_password(v_password, usuario.password)
    if not pass_valido:
        return Response("Password Incorecta")
    
    token, created = Token.objects.get_or_create(user=usuario)
    return Response(token.key)
