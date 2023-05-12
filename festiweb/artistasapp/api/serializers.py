from rest_framework import serializers
from artistasapp.models import *


class ArtistaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = (
         '__all__'

          
        )

      

class ArtistaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Artista
        fields=(
           '__all__'
        )

class ContactoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = (
         '__all__'

          
        )

      

class ContactoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contacto
        fields=(
           '__all__'
        )

