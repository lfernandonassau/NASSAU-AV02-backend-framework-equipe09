from django.db import models

class Parceiros(models.Model):
    matricula = models.CharField(primary_key=True)
    nome = models.CharField(max_length=100)
    
