from rest_framework import serializers
from artistasapp.models import *

# Serializador para la lista de artistas
class ArtistaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = (
         '__all__'

          
        )

      
# Serializador para el detalle de un artista
class ArtistaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Artista
        fields=(
           '__all__'
        )
# Serializador para la lista de contactos
class ContactoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = (
         '__all__'

          
        )

      
# Serializador para el detalle de un contacto
class ContactoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contacto
        fields=(
           '__all__'
        )

