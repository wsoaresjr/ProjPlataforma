from django.db import models

class Programa(models.Model):
    cod_programa = models.CharField(max_length=10, primary_key=True)
    programa = models.CharField(max_length=200)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    nome_contato = models.CharField(max_length=150)
    telefone_contato = models.CharField(max_length=15)
    email_contato = models.EmailField()
    qtd_testes = models.PositiveIntegerField()
    contrato_assinado = models.BooleanField(default=False)
    arquivo_contrato = models.FileField(upload_to='contratos/', blank=True, null=True)
    observacoes = models.TextField(max_length=700, blank=True)

    def __str__(self):
        return self.programa
