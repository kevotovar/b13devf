from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    url(r'^users/', include('modules.Publicaciones.urls_api')),
    url(r'^auth/', obtain_jwt_token),
    url(r'auth/refresh', refresh_jwt_token)
]