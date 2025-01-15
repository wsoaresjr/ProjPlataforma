# Generated by Django 5.1.4 on 2025-01-15 20:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('disciplinas', '0002_rename_eixo_disciplina_area_conhecimento_and_more'),
        ('padrao_item', '0001_initial'),
        ('tipo_item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subprograma',
            fields=[
                ('cod_subprograma', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('subprograma', models.CharField(max_length=200)),
                ('data_aplicacao', models.DateField()),
                ('qtd_itens', models.PositiveIntegerField()),
                ('disciplinas_avaliadas', models.ManyToManyField(related_name='subprogramas', to='disciplinas.disciplina')),
                ('padrao_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subprogramas', to='padrao_item.padraoitem')),
                ('tipo_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subprogramas', to='tipo_item.tipoitem')),
            ],
        ),
    ]
