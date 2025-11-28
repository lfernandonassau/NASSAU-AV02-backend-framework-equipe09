from rest_framework import serializers
from .models import HistoricoSimulacao

class HistoricoSimulacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoSimulacao
        fields = ['prazo', 
                  'margem_cliente', 
                  'valor_liberado', 
                  'parcela', 
                  'comissao_parceiro_valor', 
                  'data_registro' 
                  ]
        read_only_fields = fields
        
    
    def create(self, validated_data):
        raise serializers.ValidationError("Criação de histórico via API não permitida; este endpoint é apenas para leitura.")