from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm

# Create your views here.

def Index(request):
    user = request.user
    return render(request,'Home/index.html',{'user':user})

def Contacto(request):
    return HttpResponse('Contactame pls')

def Otros(request,num):
    return HttpResponse('Pagina de otros numero ' + num)

def Login(request):
    #Se envian los datos del usuario y se validan
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            login(request,user)
            return redirect('Home:index')
        else:
            return HttpResponse('Error en usuario o contraseña')
    else:
        return render(request,'Home/login.html')

def Logout(request):
    logout(request)
    return redirect('Home:index')


def Signup(request):
    #Se envian los datos al POST del signup
    if request.method == 'POST':
        #Se asignan las variables capturadas del form
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        #Verificacion si el nombre de usuario ya existe
        user = User.objects.get(username=username)
        if user is None:
            #Se crea el usuario
            user = User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                username = username,
                password = password,
                email = email
            )
            user.save()
            return HttpResponse('Usuario registrado')
        else:
            #Se manda un mensaje de error
            return HttpResponse('El usuario ya existe')

    else:

        return render(request,'Home/signup.html')
