from django.conf.urls import url
from .views import Index, Add

urlpatterns = [
    url(r'^$', Index, name='index'),
    url(r'^add$', Add, name='add')
]
