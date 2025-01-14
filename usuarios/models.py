from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Usuario(models.Model):
    cod_usuario = models.CharField(max_length=4, primary_key=True)
    nome = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    senha = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)
    chave_pix = models.CharField(max_length=100, null=True, blank=True)
    status_ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    def set_password(self, raw_password):
        self.senha = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.senha)
