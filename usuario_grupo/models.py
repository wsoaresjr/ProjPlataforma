from django.db import models
from usuarios.models import Usuario
from grupos.models import Grupo

class UsuarioGrupo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.nome} - {self.grupo.nome_grupo}"
