from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Publicacion

class UserSecondSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('is_active',)

class PublicacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publicacion
        fields = ('id','nombre','contenido','tags')

class PublicacionSecondSerializer(serializers.ModelSerializer):
    #writer = serializers.CharField(source = 'autor.username')
    class Meta:
        model = Publicacion
        fields = ('id','nombre','contenido','tags','autor','imagen')

class UserSerializer(serializers.ModelSerializer):
    publicaciones = PublicacionSerializer(read_only = True, many = True)
    class Meta:
        model = User
        fields = (
            'pk',
            'first_name',
            'last_name',
            'username',
            'email',
            'publicaciones',
            )
        #todos los campos field = ('__ALL__')
