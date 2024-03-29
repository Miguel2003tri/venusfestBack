# Generated by Django 3.2 on 2023-05-11 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artistasapp', '0005_alter_artista_foto_artista'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128, verbose_name='Nombre')),
                ('telf', models.CharField(default='', max_length=16, verbose_name='Telf')),
                ('email', models.EmailField(default='', max_length=128, verbose_name='Email')),
                ('asunto', models.TextField(blank=True, default='', null=True, verbose_name='Asunto')),
                ('mensaje', models.TextField(blank=True, default='', null=True, verbose_name='Mensaje')),
            ],
        ),
    ]
