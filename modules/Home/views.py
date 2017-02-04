from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Index(request):
    return render(request,'Home/index.html')

def Contacto(request):
    return HttpResponse('Contactame pls')

def Otros(request,num):
    return HttpResponse('Pagina de otros numero ' + num)

def Suma(request,num1,num2):
    num1 = int(num1)
    num2 = int(num2)
    suma = str(num1 + num2)
    return HttpResponse('La suma de ' + str(num1) + ' más ' + str(num2) + ' es igual a ' + suma)

def Comparacion(request,num1,num2):
    num1 = int(num1)
    num2 = int(num2)
    if num1 > num2:
        return HttpResponse('El mayor es ' + str(num1))
    elif num1 < num2:
        return HttpResponse('El mayor es ' + str(num2))
    else:
        return HttpResponse('Son iguales')

def Nombre(request,nombre):
    return HttpResponse('Hola ' + nombre)