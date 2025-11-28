from django.shortcuts import render
from rest_framework import viewsets
from .models import HistoricoSimulacao
from .serializers import HistoricoSimulacaoSerializer

# Create your views here.
class HistoricoSimulacaoViewSet(viewsets.ModelViewSet):
    queryset = HistoricoSimulacao.objects.all()
    serializer_class = HistoricoSimulacaoSerializer