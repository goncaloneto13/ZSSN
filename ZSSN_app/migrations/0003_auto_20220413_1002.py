# Generated by Django 3.2.13 on 2022-04-13 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZSSN_app', '0002_rename_name_sobrevivente_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='sobrevivente',
            name='infectado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sobrevivente',
            name='lat',
            field=models.DecimalField(decimal_places=6, default=False, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sobrevivente',
            name='log',
            field=models.DecimalField(decimal_places=6, default=11, max_digits=9),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sobrevivente',
            name='idade',
            field=models.DecimalField(decimal_places=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='sobrevivente',
            name='sexo',
            field=models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino')], max_length=1),
        ),
    ]