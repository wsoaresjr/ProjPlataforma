from django.db import models
from disciplinas.models import Disciplina
from etapas.models import Etapa
from matrizes.models import Matriz
from padrao_item.models import PadraoItem
from tipo_item.models import TipoItem
from descritores.models import Descritor
from usuarios.models import Usuario

class Demanda(models.Model):
    cod_demanda = models.CharField(max_length=10, primary_key=True)
    nome_demanda = models.CharField(max_length=100)
    observacoes = models.TextField(max_length=700, blank=True)

    def __str__(self):
        return self.nome_demanda

class Item(models.Model):
    cod_item = models.CharField(max_length=20, primary_key=True)
    demanda = models.ForeignKey(Demanda, on_delete=models.CASCADE, related_name='itens')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)
    matriz = models.ForeignKey(Matriz, on_delete=models.CASCADE)
    padrao_item = models.ForeignKey(PadraoItem, on_delete=models.CASCADE)
    tipo_item = models.ForeignKey(TipoItem, on_delete=models.CASCADE)
    descritor = models.ForeignKey(Descritor, on_delete=models.CASCADE)
    qtd_itens = models.PositiveIntegerField()
    elaborador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='elaborador')
    revisor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='revisor')
    status_item = models.CharField(max_length=20, default="A Elaborar")

    def __str__(self):
        return self.cod_item
