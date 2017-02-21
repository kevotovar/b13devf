from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework_swagger.views import get_swagger_view

api_docs = get_swagger_view('Blog API Docs')

urlpatterns = [
    url(r'^users/', include('modules.Publicaciones.urls_api')),
    url(r'^auth/', obtain_jwt_token),
    url(r'^auth/refresh', refresh_jwt_token),
    url(r'^docs/', api_docs),
]