from django.shortcuts import render

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
