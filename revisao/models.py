from django.db import models
from usuarios.models import Usuario
from demandas.models import Item  # <- ESTE IMPORT TEM QUE EXISTIR

class ItemRevisor(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    revisor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="itens_designados")
    data_designacao = models.DateField(auto_now_add=True)
    comentario = models.TextField(blank=True, null=True)
    # outros campos se quiser





