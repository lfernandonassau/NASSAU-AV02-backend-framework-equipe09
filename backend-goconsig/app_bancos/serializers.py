from rest_framework import serializers
from .models import Banco

class BancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banco
        fields = ['codigo_banco', 'nome', 'fator', 'comissao_parceiro']