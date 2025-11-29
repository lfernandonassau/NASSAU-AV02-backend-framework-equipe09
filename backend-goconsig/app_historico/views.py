from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .models import HistoricoSimulacao
from .serializers import HistoricoSimulacaoSerializer

# Create your views here.
class HistoricoSimulacaoListAPIView(generics.ListAPIView):
    serializer_class = HistoricoSimulacaoSerializer
    # Apenas administradores podem visualizar o histórico
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        qs = HistoricoSimulacao.objects.select_related('cliente', 'simulacao').all().order_by('-data_registro')
        sim_id = self.kwargs.get('sim_id') or self.request.query_params.get('sim_id')
        if sim_id:
            # ajuste 'simulacao' abaixo para o nome real da FK no model (ex: 'simulacao' ou 'simulacao_id')
            return qs.filter(simulacao_id=sim_id)
        # Sem sim_id: retorna todo o histórico (apenas admins)
        return qs