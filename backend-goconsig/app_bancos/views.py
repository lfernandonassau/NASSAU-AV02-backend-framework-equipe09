from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Banco
from .serializers import BancoSerializer

# Create your views here.
class ViewSet(viewsets.ModelViewSet):
    queryset = Banco.objects.all()
    serializer_class = BancoSerializer