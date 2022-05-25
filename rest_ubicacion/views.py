from django.shortcuts import render
from rest_framework import status #(codigo de error o exit)
from rest_framework.decorators import api_view #(listar registros)
from rest_framework.response import Response #(dar respuesta)
from rest_framework.parsers import JSONParser #(convertir llos objetos en json)
from django.views.decorators.csrf import csrf_exempt #(seguridad)
from Telefonos.models import Sucursal
from rest_ubicacion.serializers import SucursalSerializer

@csrf_exempt 
@api_view(['GET','POST'])
def lista_sucursales(request):
    if request.method == 'GET':
        listaSucursal = Sucursal.objects.all()
        serializ = SucursalSerializer(listaSucursal, many= True)
        return Response (serializ.data)
    elif request.method == 'POST':
        dataS = JSONParser().parse(request)
        serializ = SucursalSerializer(data = dataS)
        if serializ.is_valid():
            serializ.save()
            return Response(serializ.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializ.errors, status = status.HTTP_400_BAD_REQUEST)

