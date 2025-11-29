from django.shortcuts import render
from rest_framework import viewsets
from .models import Parceiro
from .serializers import ParceiroSerializer
# Create your views here.
class ParceiroViewSet(viewsets.ModelViewSet):
    queryset = Parceiro.objects.all()
    serializer_class = ParceiroSerializer
