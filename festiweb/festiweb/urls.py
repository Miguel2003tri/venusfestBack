"""festiweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework import routers
from artistasapp.api import views as artistas_api_views

router = routers.DefaultRouter()

router.register(r'artista_list',artistas_api_views.ArtistaListViewSet,basename='artista_list')
router.register(r'artista_detail',artistas_api_views.ArtistaDetailViewSet,basename='artista_detail')
router.register(r'contacto_list',artistas_api_views.ContactoListViewSet,basename='contacto_list')
router.register(r'contacto_detail',artistas_api_views.ContactoDetailViewSet,basename='contacto_detail')

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
