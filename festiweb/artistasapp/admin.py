from django.contrib import admin
from .models import Artista,Contacto

class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'nombre_artistico', 'email', 'telf', 'direccion_postal', 'descripcion_proyecto', 'enlaces_redes_sociales', 'experiencia_previa', 'requerimientos_tecnicos', 'disponibilidad', 'condiciones_participacion')
    list_display_links=( 'nombre', 'nombre_artistico', 'email', 'telf', 'direccion_postal', 'descripcion_proyecto', 'enlaces_redes_sociales', 'experiencia_previa', 'requerimientos_tecnicos', 'disponibilidad', 'condiciones_participacion')
    search_fields = ('nombre', 'nombre_artistico', 'email', 'telf', 'direccion_postal', 'descripcion_proyecto', 'enlaces_redes_sociales', 'experiencia_previa', 'requerimientos_tecnicos', 'disponibilidad', 'condiciones_participacion')

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'nombre', 'email', 'asunto', 'mensaje')
    list_display_links=( 'nombre', 'nombre', 'email', 'asunto', 'mensaje')
    search_fields = ('nombre', 'nombre', 'email', 'asunto', 'mensaje')


admin.site.register(Artista, ArtistaAdmin)
admin.site.register(Contacto, ContactoAdmin)
