from django.db import models
from disciplinas.models import Disciplina
from tipo_item.models import TipoItem
from padrao_item.models import PadraoItem
from programas.models import Programa
from etapas.models import Etapa

class Subprograma(models.Model):
    cod_subprograma = models.CharField(max_length=10, primary_key=True)
    subprograma = models.CharField(max_length=200)
    data_aplicacao = models.DateField()
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name='subprogramas', default=1)
    disciplinas_avaliadas = models.ManyToManyField(Disciplina, related_name='subprogramas')
    qtd_itens = models.PositiveIntegerField()
    tipo_item = models.ForeignKey(TipoItem, on_delete=models.CASCADE, related_name='subprogramas')
    padrao_item = models.ForeignKey(PadraoItem, on_delete=models.CASCADE, related_name='subprogramas')
    etapas_avaliadas = models.ManyToManyField(Etapa, related_name='subprogramas')

    def __str__(self):
        return self.subprograma
