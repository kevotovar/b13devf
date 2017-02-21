from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, filters
from django.contrib.auth.models import User
from modules.Publicaciones.models import Publicacion
from .serializers import UserSerializer,UserSecondSerializer,PublicacionSecondSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .permisssions import GroupPermission

#Vistas basadas en clases

class UserList(APIView):
    
    def get(self,request):
        #Se pide todo los usuarios
        user = User.objects.all()
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request):
        #Se crea el usuario
        serializer = UserSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):

    def get(self,request,pk):
        user = get_object_or_404(User, pk=pk)

        if user is not None:
            serializer = UserSerializer(user)
            return Response(serializer.data,status=status.HTTP_200_OK)        
    
    def put(self,request,pk):
        user = get_object_or_404(User,pk=pk)

        if user is not None:
            serializer = UserSerializer(instance=user,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        user = get_object_or_404(User, pk=pk)

        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class PublicacionList(generics.ListCreateAPIView):
    
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSecondSerializer
    permission_classes = (AllowAny,)
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    filter_fields = ('fecha',)
    search_fields = ('nombre', 'tags')


    """def get_queryset(self):

        queryset = Publicacion.objects.all()
        name = self.request.query_params.get('publicacion',None)
        if name is not None:
            queryset = Publicacion.objects.filter(nombre__icontains = name)
        
        return queryset"""


class PublicacionDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSecondSerializer
    #Agrega la restriccion que debe ser administrador
    permission_classes = (GroupPermission,)
