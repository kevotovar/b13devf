from django.conf.urls import url
from .api_views import UserList

urlpatterns = [
    url(r'^$', UserList.as_view()),
]