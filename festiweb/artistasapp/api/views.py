#UD11.3.a
from rest_framework import (mixins, 
                            permissions, 
                            viewsets, 
                            filters, 
                            views, 
                            response, 
                            status)
from .serializers import *
from rest_framework.response import Response
from artistasapp.models import *
#Artista

class ArtistaListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):

    """
    Todos los datos de los Artistas de la aplicacin
    """
    serializer_class = ArtistaListSerializer
    filter_backends=(filters.OrderingFilter, filters.SearchFilter)
    ordering= 'nombre'
    search_fields = ['nombre']

    def get_queryset(self):
        return Artista.objects.all()

#Artista

class ArtistaDetailViewSet(viewsets.ModelViewSet):
    """
    Comentario
    """
    serializer_class=ArtistaDetailSerializer
    queryset=Artista.objects.all()
    
    def create(self, req):
        print("Creado", req.data)
        artista = Artista(**req.data)
        artista.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self):
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, *args, **kwargs):
       instance = self.get_object()
       try:
           self.perform_destroy(instance)
       except Exception as e:
           return Response({"error": "No se puede realizar la operación de borrado porque existen dependencias." + str(e)}, status=status.HTTP_400_BAD_REQUEST)
       return Response(status=status.HTTP_204_NO_CONTENT)

#Contacto
class ContactoListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):

    """
    Todas las consultas de contacto    
    """
    serializer_class = ContactoListSerializer
    filter_backends=(filters.OrderingFilter, filters.SearchFilter)
    ordering= 'nombre'
    search_fields = ['nombre']

    def get_queryset(self):
        return Contacto.objects.all()

#Contacto
class ContactoDetailViewSet(viewsets.ModelViewSet):
    """
    Todas las consultas de contacto    
    """
    serializer_class=ContactoDetailSerializer
    queryset=Contacto.objects.all()
    
    def create(self, req):
        print("Creado", req.data)
        contacto = Contacto(**req.data)
        contacto.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self):
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, *args, **kwargs):
       instance = self.get_object()
       try:
           self.perform_destroy(instance)
       except Exception as e:
           return Response({"error": "No se puede realizar la operación de borrado porque existen dependencias." + str(e)}, status=status.HTTP_400_BAD_REQUEST)
       return Response(status=status.HTTP_204_NO_CONTENT)

