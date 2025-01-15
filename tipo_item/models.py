from django.db import models

class TipoItem(models.Model):
    cod_tipo_item = models.CharField(max_length=10, primary_key=True)
    tipo_item = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo_item
