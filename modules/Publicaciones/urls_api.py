from django.conf.urls import url
from .api_views import UserList,UserDetail,PublicacionList,PublicacionDetail

urlpatterns = [
    url(r'^$', UserList.as_view()),
    url(r'^publicacion/$', PublicacionList.as_view(), name = 'api-publicacion-list'),
    url(r'^publicacion/(?P<pk>[0-9])+$', PublicacionDetail.as_view(), name = 'api-publicacion-detail'),
    url(r'^(?P<pk>[0-9])+$', UserDetail.as_view()),
]