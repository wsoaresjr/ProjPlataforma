from django.db import models
from disciplinas.models import Disciplina
from tipo_item.models import TipoItem
from padrao_item.models import PadraoItem

class Subprograma(models.Model):
    cod_subprograma = models.CharField(max_length=10, primary_key=True)
    subprograma = models.CharField(max_length=200)
    data_aplicacao = models.DateField()
    disciplinas_avaliadas = models.ManyToManyField(Disciplina, related_name='subprogramas')
    qtd_itens = models.PositiveIntegerField()
    tipo_item = models.ForeignKey(TipoItem, on_delete=models.CASCADE, related_name='subprogramas')
    padrao_item = models.ForeignKey(PadraoItem, on_delete=models.CASCADE, related_name='subprogramas')

    def __str__(self):
        return self.subprograma
