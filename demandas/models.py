from django.db import models
from disciplinas.models import Disciplina
from etapas.models import Etapa
from matrizes.models import Matriz
from padrao_item.models import PadraoItem
from tipo_item.models import TipoItem
from descritores.models import Descritor
from usuarios.models import Usuario
from django.utils import timezone
from django_quill.fields import QuillField

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
    data_elaborador = models.DateField(null=True, blank=True)
    revisor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='revisor')
    data_revisor = models.DateField(null=True, blank=True)
    status_item = models.CharField(max_length=20, default="A Elaborar")
    consideracoes_revisor = QuillField(null=True, blank=True)

    def __str__(self):
        return self.cod_item

    def calcular_status(self, data):
            if not data:
                return "Sem Prazo"
            hoje = timezone.now().date()
            dias_restantes = (data - hoje).days

            if dias_restantes > 2:
                return "No prazo", "green"
            elif dias_restantes == 2:
                return "Prazo terminando", "blue"
            elif dias_restantes == 0:
                return "Prazo termina hoje!", "orange"
            else:
                return "Prazo expirado", "red"

    @property
    def status_elaborador(self):
        return self.calcular_status(self.data_elaborador)

    @property
    def status_revisor(self):
        return self.calcular_status(self.data_revisor)