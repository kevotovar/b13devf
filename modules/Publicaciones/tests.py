from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Publicacion
from django.contrib.auth.models import User
import json

# Create your tests here.

class PublicacionTest(APITestCase):
    #Cuando se crea el test
    def setUp(self):
        self.user = User.objects.create_superuser(username="kevin", email = "kevintovar@esimez.mx", password = "blog123456")
        self.data = {"nombre":"otra Publicacion", "contenido":"ajjajajajajjajajaj","tags":"TC","autor":self.user.id}
        self.url = reverse('api-publicacion-list')
    
    def test_list_publicaciones(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_publicaciones(self):
        response = self.client.post(self.url, self.data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class PublicacionDetailTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(username="kevin", email = "kevintovar@esimez.mx", password = "blog123456")
        self.data = {"nombre":"otra Publicacion", "contenido":"ajjajajajajjajajaj","tags":"TC","autor":self.user.id}
        self.publicacion = Publicacion(nombre = "publicacion", contenido = "jajaja", tags = 'TC', autor = self.user)
        self.publicacion.save()
        self.url = reverse('api-publicacion-detail', args = [self.publicacion.id])

    def test_retrieve_publicacion(self):
        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update_publicacion(self):
        self.data = {"nombre":"publicacion modificada", "contenido":"ajjajajajajjajajaj","tags":"TC","autor":self.user.id}
        response = self.client.put(self.url, data = self.data, format = "json")
        print(str(User.objects.all()))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete_publicacion(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
