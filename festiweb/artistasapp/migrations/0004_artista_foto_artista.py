# Generated by Django 3.2 on 2023-05-06 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artistasapp', '0003_auto_20230502_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='artista',
            name='foto_artista',
            field=models.ImageField(blank=True, upload_to='artistas/', verbose_name='Foto del artista'),
        ),
    ]
