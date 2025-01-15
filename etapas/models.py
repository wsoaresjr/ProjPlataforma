from django.db import models
from ensinos.models import Ensino

class Etapa(models.Model):
    cod_etapa = models.CharField(max_length=10, primary_key=True)
    etapa = models.CharField(max_length=100)
    ensino = models.ForeignKey(Ensino, on_delete=models.CASCADE, related_name='etapas')

    def __str__(self):
        return f"{self.etapa} ({self.ensino.ensino})"
