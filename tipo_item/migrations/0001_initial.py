# Generated by Django 5.1.4 on 2025-01-15 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoItem',
            fields=[
                ('cod_tipo_item', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('tipo_item', models.CharField(max_length=100)),
            ],
        ),
    ]