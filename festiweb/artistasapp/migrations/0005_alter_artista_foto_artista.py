# Generated by Django 3.2 on 2023-05-08 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artistasapp', '0004_artista_foto_artista'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='foto_artista',
            field=models.CharField(max_length=256, verbose_name='Images'),
        ),
    ]
