from django.db import models
from demandas.models import Item
from django_quill.fields import QuillField

class ElaboracaoItem(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, related_name='elaboracao')
    gabarito = models.CharField(
        max_length=1,
        choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')],
        null=True, blank=True
    )
    conteudo = QuillField(null=True, blank=True)
    comando = QuillField(null=True, blank=True)
    alternativa_a = QuillField(null=True, blank=True)
    alternativa_b = QuillField(null=True, blank=True)
    alternativa_c = QuillField(null=True, blank=True)
    alternativa_d = QuillField(null=True, blank=True)
    alternativa_e = QuillField(null=True, blank=True)
    justificativa_a = QuillField(null=True, blank=True)
    justificativa_b = QuillField(null=True, blank=True)
    justificativa_c = QuillField(null=True, blank=True)
    justificativa_d = QuillField(null=True, blank=True)
    justificativa_e = QuillField(null=True, blank=True)

    def __str__(self):
        return f"Elaboração do Item {self.item.cod_item}"
