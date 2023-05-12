# Generated by Django 3.2 on 2023-05-02 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artistasapp', '0002_alter_artista_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artista',
            name='apellidos',
        ),
        migrations.RemoveField(
            model_name='artista',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='artista',
            name='horario_particip',
        ),
        migrations.RemoveField(
            model_name='artista',
            name='img',
        ),
        migrations.RemoveField(
            model_name='artista',
            name='tipo',
        ),
        migrations.AddField(
            model_name='artista',
            name='condiciones_participacion',
            field=models.CharField(blank=True, default='', max_length=256, null=True, verbose_name='Condiciones de participacion'),
        ),
        migrations.AddField(
            model_name='artista',
            name='descripcion_proyecto',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Descripción del proyecto'),
        ),
        migrations.AddField(
            model_name='artista',
            name='direccion_postal',
            field=models.CharField(blank=True, default='', max_length=256, null=True, verbose_name='Dirección postal'),
        ),
        migrations.AddField(
            model_name='artista',
            name='disponibilidad',
            field=models.CharField(default='', max_length=128, verbose_name='Disponibilidad'),
        ),
        migrations.AddField(
            model_name='artista',
            name='enlaces_redes_sociales',
            field=models.URLField(default='', max_length=256, verbose_name='Enlaces a redes sociales'),
        ),
        migrations.AddField(
            model_name='artista',
            name='experiencia_previa',
            field=models.TextField(default='', max_length=256, verbose_name='Experiencia previa'),
        ),
        migrations.AddField(
            model_name='artista',
            name='nombre_artistico',
            field=models.CharField(default='', max_length=256, verbose_name='Nombre artístico'),
        ),
        migrations.AddField(
            model_name='artista',
            name='requerimientos_tecnicos',
            field=models.TextField(default='', max_length=256, verbose_name='Requerimientos técnicos'),
        ),
        migrations.AddField(
            model_name='artista',
            name='telf',
            field=models.CharField(default='', max_length=16, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='artista',
            name='email',
            field=models.EmailField(default='', max_length=128, verbose_name='Correo electrónico'),
        ),
    ]
