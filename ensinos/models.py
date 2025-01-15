from django.db import models

class Ensino(models.Model):
    cod_ensino = models.CharField(max_length=10, primary_key=True)
    ensino = models.CharField(max_length=100)

    def __str__(self):
        return self.ensino
