# Generated by Django 3.2.13 on 2022-04-16 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZSSN_app', '0009_alter_sobrevivente_infectados_relatados'),
    ]

    operations = [
        migrations.AddField(
            model_name='sobrevivente',
            name='data_n',
            field=models.DateField(default='1998-08-13', verbose_name='Data de Nascimento'),
            preserve_default=False,
        ),
    ]
