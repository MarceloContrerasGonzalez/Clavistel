import imp
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from Telefonos.models import Movil
from rest_ubicacion.serializers import TelefonoSerializer

# Create your views here.
