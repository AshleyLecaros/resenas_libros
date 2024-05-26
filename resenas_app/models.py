from django.db import models
from django.utils import timezone

# Create your models here.

class Autores(models.Model):
    autores_id = models.AutoField(primary_key=True) # por defecto no puede ser nulo, y es unico. 
    nombre = models.CharField(max_length=50, null=False, blank=False, unique=True)
    
    def __str__(self):
        return self.nombre
    

class Genero(models.Model):
    genero_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False, unique=True)
    
    def __str__(self):
        return self.nombre
    

class Libros(models.Model):
    libros_id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50, null=False, blank=False, unique=True)
    descripcion = models.TextField(max_length=300)
    año_publicacion = models.IntegerField()
    portada_url = models.URLField()
    genero_id = models.ForeignKey('genero', on_delete=models.CASCADE,related_name='libros', null=False, blank=False)
    autores_id = models.ForeignKey('autores', on_delete=models.CASCADE,related_name='libros', null=False, blank=False)
    
    def __str__(self):
        return f"{self.titulo} - {self.descripcion}, {self.autores_id.nombre}"
    
class Usuarios(models.Model):
    usuarios_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False, unique=True, default='')
    password = models.CharField(max_length=50, null=False, blank=False)
    tipo_usuario = models.CharField(default='Lector')
    
    def __str__(self):
        return f"{self.nombre} - {self.email}"
    

class Reseñas(models.Model):
    reseña_id = models.AutoField(primary_key=True)
    libro_id = models.ForeignKey('Libros', on_delete=models.CASCADE,related_name='reseñas', null=False, blank=False)
    usuario_id = models.ForeignKey('Usuarios', on_delete=models.CASCADE,related_name='reseñas', null=False, blank=False)
    calificacion = models.IntegerField(null=False, blank=False)
    comentario = models.TextField()
    fecha_reseña = models.DateTimeField(default=timezone.now)
    
        
    def __str__(self):
        return f"{self.comentario}, {self.calificacion}, {self.fecha_reseña}, {self.usuario_id.nombre}"

    
    

