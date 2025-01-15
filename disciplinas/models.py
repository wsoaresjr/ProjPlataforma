from django.db import models

class Disciplina(models.Model):
    cod_disciplina = models.CharField(max_length=10, primary_key=True)
    disciplina = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10)
    area_conhecimento = models.CharField(max_length=100)

    def __str__(self):
        return self.disciplina
