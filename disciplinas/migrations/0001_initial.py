# Generated by Django 5.1.4 on 2025-01-15 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('cod_disciplina', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('disciplina', models.CharField(max_length=100)),
                ('cod_eixo', models.CharField(max_length=10)),
                ('eixo', models.CharField(max_length=100)),
            ],
        ),
    ]