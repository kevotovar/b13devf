from django.db import models
from django.contrib.auth.models import User

TAGS = (
    ('TC','Tecnología'),
    ('CT','Cientifico'),
    ('PR','Programacion'),
)

#Manager de Publicaciones
'''
class LoloPublicacionesManager(models.Manager):

    def get_queryset(self):
        return super(LoloPublicacionesManager,self).get_queryset().filter(autor__username='lolo')
'''
#Clase de modelo principal
class Publicacion (models.Model):
    # Generador de id primaria(
    id = models.AutoField(primary_key = True)
    # Varchar con un recomendado de 50 caracteres
    nombre = models.CharField(max_length = 50)
    # Area de texto descriptivo
    contenido = models.TextField()
    # Timestamps
    fecha = models.DateField(auto_now_add=True)
    # Relación 1 a muchos inversa
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    # Enum
    tags = models.CharField(choices=TAGS,max_length=50)
    # Llamado al Manager
    #lolo_publish = LoloPublicacionesManager()

    def __str__(self):
        return "%s %s" % ("Publicacion: ", self.nombre)
