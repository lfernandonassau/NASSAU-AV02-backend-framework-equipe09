from rest_framework.viewsets import ModelViewSet
from app_emprestimos.models import Simulacao
from app_emprestimos.serializers import SimulacaoSerializer


class SimulacaoViewSet(ModelViewSet): 
    queryset = Simulacao.objects.all()
    serializer_class = SimulacaoSerializer
