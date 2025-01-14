from django.db import models

class Grupo(models.Model):
    cod_grupo = models.CharField(max_length=3, primary_key=True)
    nome_grupo = models.CharField(max_length=80)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome_grupo
