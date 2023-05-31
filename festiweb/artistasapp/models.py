from django.db import models
# Modelo Artista
class Artista(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=128)
    nombre_artistico = models.CharField(verbose_name='Nombre artístico', max_length=256,default='')
    email = models.EmailField(verbose_name='Correo electrónico', max_length=128,default='')
    telf = models.CharField(verbose_name='Teléfono', max_length=16,default='')
    direccion_postal = models.CharField(verbose_name='Dirección postal', max_length=256 ,blank=True, null=True, default='')
    descripcion_proyecto = models.TextField(verbose_name='Descripción del proyecto',blank=True, null=True, default='')
    enlaces_redes_sociales = models.URLField(verbose_name='Enlaces a redes sociales', max_length=256,default='')
    experiencia_previa = models.TextField(verbose_name='Experiencia previa',max_length=256, default='')
    requerimientos_tecnicos = models.TextField(verbose_name='Requerimientos técnicos',max_length=256, default='')
    disponibilidad = models.CharField(verbose_name='Disponibilidad', max_length=128,default='')
    condiciones_participacion = models.CharField(verbose_name='Condiciones de participacion',max_length=256, blank=True, null=True, default='')
    foto_artista = models.CharField(verbose_name='Images', max_length=256)


# Modelo Contacto
class Contacto(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=128)
    telf = models.CharField(verbose_name='Telf', max_length=16,default='')
    email = models.EmailField(verbose_name='Email', max_length=128,default='')
    asunto = models.TextField(verbose_name='Asunto',blank=True, null=True, default='')
    mensaje = models.TextField(verbose_name='Mensaje',blank=True, null=True, default='')

