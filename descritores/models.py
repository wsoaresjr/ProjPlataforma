from django.db import models
from disciplinas.models import Disciplina

class Descritor(models.Model):
    cod_descritor = models.CharField(max_length=10, primary_key=True)
    descritor = models.TextField(max_length=350)
    cod_eixo = models.CharField(max_length=10)
    eixo = models.CharField(max_length=100)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='descritores')

    def __str__(self):
        return f"{self.cod_descritor} - {self.descritor[:50]}..."
