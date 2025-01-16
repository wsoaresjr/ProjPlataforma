from django.db import models
from programas.models import Programa
from subprogramas.models import Subprograma
from disciplinas.models import Disciplina
from descritores.models import Descritor
from etapas.models import Etapa

class Matriz(models.Model):
    cod_matriz = models.CharField(max_length=10, primary_key=True)
    matriz = models.CharField(max_length=200)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name='matrizes')
    subprograma = models.ForeignKey(Subprograma, on_delete=models.CASCADE, related_name='matrizes')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='matrizes')
    descritores = models.ManyToManyField(Descritor, related_name='matrizes')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE, related_name='matrizes')

    def __str__(self):
        return self.matriz

