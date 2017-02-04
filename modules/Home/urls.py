from django.conf.urls import url
from .views import Index,Contacto,Otros,Suma,Nombre,Comparacion
'''
Suma
Nombre
Comparacion mayor
'''
urlpatterns = [
    url(r'^$', Index, name='index'),
    url(r'^contacto$', Contacto, name='contacto'),
    url(r'^nombre/(?P<nombre>[a-zA-Z]+)/$', Nombre, name='nombre'),
    url(r'^otros/(?P<num>[0-9]+)/$', Otros, name='otros'),
    url(r'^suma/(?P<num1>[0-9]+)/(?P<num2>[0-9]+)/$', Suma, name='suma'),
    url(r'^comparacion/(?P<num1>[0-9]+)/(?P<num2>[0-9]+)/$', Comparacion, name='comparacion')
    #url(r'^$', admin.site.urls),
]