# Generated by Django 5.1.4 on 2025-01-16 17:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programas', '0001_initial'),
        ('subprogramas', '0001_initial'),
    ]

    operations = [
    migrations.AddField(
        model_name='subprograma',
        name='programa',
        field=models.ForeignKey(
            default='AM1',  # Use o código do programa existente
            on_delete=models.CASCADE,
            related_name='subprogramas',
            to='programas.Programa',
        ),
        preserve_default=False,
        ),
    ]