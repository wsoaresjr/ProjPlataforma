# Generated by Django 5.1.4 on 2025-01-15 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('cod_programa', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('programa', models.CharField(max_length=200)),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
                ('nome_contato', models.CharField(max_length=150)),
                ('telefone_contato', models.CharField(max_length=15)),
                ('email_contato', models.EmailField(max_length=254)),
                ('qtd_testes', models.PositiveIntegerField()),
                ('contrato_assinado', models.BooleanField(default=False)),
                ('arquivo_contrato', models.FileField(blank=True, null=True, upload_to='contratos/')),
                ('observacoes', models.TextField(blank=True, max_length=700)),
            ],
        ),
    ]
