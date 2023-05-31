from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework import routers
from artistasapp.api import views as artistas_api_views
# Definición de los routers para las vistas de la API

router = routers.DefaultRouter()
# Registro de las vistas de la API en los routers

router.register(r'artista_list',artistas_api_views.ArtistaListViewSet,basename='artista_list')
router.register(r'artista_detail',artistas_api_views.ArtistaDetailViewSet,basename='artista_detail')
router.register(r'contacto_list',artistas_api_views.ContactoListViewSet,basename='contacto_list')
router.register(r'contacto_detail',artistas_api_views.ContactoDetailViewSet,basename='contacto_detail')
# Configuración de las URLs

urlpatterns = [
    # URLs para la autenticación de la API

    path('api-auth/', include('rest_framework.urls')),
    # URLs para las vistas de la API registradas en los routers

    path('api/', include(router.urls)),
    # URL para el panel de administración
    path('admin/', admin.site.urls),
]
