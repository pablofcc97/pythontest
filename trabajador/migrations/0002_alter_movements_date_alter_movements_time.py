# Generated by Django 5.0.1 on 2024-01-15 21:06

import trabajador.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabajador', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movements',
            name='date',
            field=models.DateTimeField(default=trabajador.models.current_date),
        ),
        migrations.AlterField(
            model_name='movements',
            name='time',
            field=models.DateTimeField(default=trabajador.models.current_time),
        ),
    ]
