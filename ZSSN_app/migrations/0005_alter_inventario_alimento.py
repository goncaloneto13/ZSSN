# Generated by Django 3.2.13 on 2022-04-16 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZSSN_app', '0004_alter_sobrevivente_inventario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='alimento',
            field=models.PositiveBigIntegerField(default=0, verbose_name='Alimentação'),
        ),
    ]