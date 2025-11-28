from rest_framework import ModelViewSet
from rest_framework import viewsets
from app_emprestimos.models import Simulacao
from app_emprestimos.serializers import SimulacaoSerializer


class SimulacaoViewSet(viewsets.ModelViewSet): 
    queryset = Simulacao.objects.all()
    serializer_class = SimulacaoSerializer
