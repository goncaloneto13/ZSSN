# Generated by Django 3.2.13 on 2022-04-13 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZSSN_app', '0003_rename_iten_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='sobrevivente',
            name='acusacoes',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
    ]