from django.db import models

class PadraoItem(models.Model):
    cod_padrao_item = models.CharField(max_length=10, primary_key=True)
    padrao_item = models.CharField(max_length=100)

    def __str__(self):
        return self.padrao_item
