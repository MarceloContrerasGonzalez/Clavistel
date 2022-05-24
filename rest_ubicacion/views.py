from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from Telefonos.models import Movil
from rest_ubicacion.serializers import TelefonoSerializer
# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])
def lista_telefonos(request):
    if request.method == 'GET':
        listaMovil = Movil.objects.all()
        serializ = TelefonoSerializer(listaMovil, many=True)
        return Response(serializ.data)
        
    elif request.method =='POST':
        dataM = JSONParser().parse(request)
        serializ == TelefonoSerializer (data=dataM)
        if serializ.is_valid():
            serializ.save()
            return Response(serializ.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializ.errors, status= status.HTTP_400_BAD_REQUEST)