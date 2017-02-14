from django.shortcuts import render,redirect
from .models import TAGS, Publicacion
from .functions import handle_uploaded_file

def Index(request):

    public = [
    {
        "nombre" : "Mi primer Proyecto en Django",
        "auto" : "Kevin Tovar",
        "fecha" : "07-02-2017",
        "rating" : 5
    },
    {
        "nombre" : "Otro Proyecto en Django",
        "auto" : "Masiosare",
        "fecha" : "07-02-2017",
        "rating" : 4
    },
    {
        "nombre" : "Ultimo Proyecto en Django",
        "auto" : "Clemente",
        "fecha" : "07-02-2017",
        "rating" : 3
    },
    ]

    return render(request,'Publicaciones/index.html',{ 'publicaciones':public })

def Add(request):

    if request.method == 'POST':
        if request.user.is_authenticated():
            types = {'image/jpeg':'.jpg','image/png':'.png','image/gif':'.gif'}
            image_name = request.FILES['imagen'].name + types[request.FILES['imagen'].content_type]
            publicacion = Publicacion()
            publicacion.nombre = request.POST['nombre']
            publicacion.contenido = request.POST['contenido']
            publicacion.tags = request.POST['tags']
            publicacion.autor = request.user
            publicacion.imagen = handle_uploaded_file(request.FILES['imagen'], image_name)

            publicacion.save()

            return redirect('Publicaciones:index')
    else:
        dict_tags = dict((x,y) for x,y in TAGS)
        return render(request, 'Publicaciones/add.html',{'tags':dict_tags})