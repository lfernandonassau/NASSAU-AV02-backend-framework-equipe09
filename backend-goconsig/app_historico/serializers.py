from rest_framework import serializers
from .models import HistoricoSimulacao

class HistoricoSimulacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoSimulacao
        fields = ['prazo', 'margem_cliente', 'valor_liberado', 'parcela', 'comissao_parceiro_valor', 'data_registro' ]