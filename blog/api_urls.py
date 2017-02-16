from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^users/', include('modules.Publicaciones.urls_api')),
    #TODO agregar Publicaciones
]