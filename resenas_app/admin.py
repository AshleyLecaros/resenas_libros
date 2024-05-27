from django.contrib import admin
from .models import Libros, Usuarios, Autores, Genero, Reseñas, ComentarioReseña

# Register your models here.
admin.site.register(Libros)
admin.site.register(Usuarios)
admin.site.register(Autores)
admin.site.register(Genero)
admin.site.register(Reseñas)
admin.site.register(ComentarioReseña)
