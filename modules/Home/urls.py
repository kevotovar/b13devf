from django.conf.urls import url
from .views import Index,Contacto,Otros,Signup,Login,Logout

urlpatterns = [
    url(r'^$', Index, name='index'),
    url(r'^contacto$', Contacto, name='contacto'),
    url(r'^otros/(?P<num>[0-9]+)/$', Otros, name='otros'),
    url(r'signup$', Signup, name='signup'),
    url(r'login$', Login, name='login'),
    url(r'logout$', Logout, name='logout')
    #url(r'^$', admin.site.urls),
]
