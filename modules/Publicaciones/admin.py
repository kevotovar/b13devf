from django.contrib import admin
from .models import Publicacion

# Para que se pueda manejar en la seccion de admin
class PublicacionAdmin(admin.ModelAdmin):
    pass
#Registro para que se pase la clase al admin
admin.site.register(Publicacion, PublicacionAdmin)
