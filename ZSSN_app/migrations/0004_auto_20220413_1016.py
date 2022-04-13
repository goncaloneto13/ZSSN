# Generated by Django 3.2.13 on 2022-04-13 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZSSN_app', '0003_auto_20220413_1002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sobrevivente',
            old_name='infectado',
            new_name='Infectado',
        ),
        migrations.RenameField(
            model_name='sobrevivente',
            old_name='lat',
            new_name='Lat',
        ),
        migrations.RenameField(
            model_name='sobrevivente',
            old_name='log',
            new_name='Log',
        ),
        migrations.RenameField(
            model_name='sobrevivente',
            old_name='nome',
            new_name='Nome',
        ),
        migrations.RenameField(
            model_name='sobrevivente',
            old_name='sexo',
            new_name='Sexo',
        ),
        migrations.RemoveField(
            model_name='sobrevivente',
            name='idade',
        ),
        migrations.AddField(
            model_name='sobrevivente',
            name='Alimento',
            field=models.PositiveBigIntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sobrevivente',
            name='Idade',
            field=models.PositiveIntegerField(default=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sobrevivente',
            name='Medicação',
            field=models.PositiveBigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sobrevivente',
            name='Munição',
            field=models.PositiveBigIntegerField(default=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sobrevivente',
            name='Água',
            field=models.PositiveIntegerField(default=3),
            preserve_default=False,
        ),
    ]