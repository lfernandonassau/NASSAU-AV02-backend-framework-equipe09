from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente
from .serializers import ClienteSerializer
'''from . models import Usuario'''
# Create your views here.
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

'''
def usuarios(request):
    novo_usuario = Usuario()
    request.POST.get('email')
    request.POST.get('cpf')
    request.POST.get('senha')
'''       