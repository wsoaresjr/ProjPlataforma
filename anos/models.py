from django.db import models

class Ano(models.Model):
    cod_ano = models.CharField(max_length=4, primary_key=True)
    ano = models.CharField(max_length=4)

    def __str__(self):
        return self.ano
