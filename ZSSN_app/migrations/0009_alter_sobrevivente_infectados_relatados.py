# Generated by Django 3.2.13 on 2022-04-16 14:21

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZSSN_app', '0008_alter_sobrevivente_infectados_relatados'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sobrevivente',
            name='infectados_relatados',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True), blank=True, default=list, size=None),
        ),
    ]
