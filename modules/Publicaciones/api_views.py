from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer,UserSecondSerializer

#Vistas basadas en clases

class UserList(APIView):
    
    def get(self,request):
        #Se pide todo los usuarios
        user = User.objects.all()
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        #Se crea el usuario
        serializer = UserSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)