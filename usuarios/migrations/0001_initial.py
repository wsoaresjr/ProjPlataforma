# Generated by Django 5.1.4 on 2025-01-14 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('cod_usuario', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('senha', models.CharField(max_length=255)),
                ('cpf', models.CharField(blank=True, max_length=11, null=True, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('chave_pix', models.CharField(blank=True, max_length=100, null=True)),
                ('status_ativo', models.BooleanField(default=True)),
            ],
        ),
    ]
