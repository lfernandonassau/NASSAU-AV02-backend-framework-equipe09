from django.shortcuts import render
from rest_framework import viewsets
from .models import Simulacao
from .serializers import SimulacaoSerializer

# Create your views here.
class ViewSet(viewsets.ModelViewSet):
    queryset = Simulacao.objects.all()
    serializer_class = SimulacaoSerializer