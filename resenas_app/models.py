from django.db import models
from django.utils import timezone
from django.db.models import Avg



# Gestor de consultas personalizado para Libros
class LibrosManager(models.Manager):
    def por_categoria(self, genero_id):
        return self.filter(genero_id=genero_id)
    
    def por_autor(self, autores_id):
        return self.filter(autores_id=autores_id)
    
    def por_calificacion(self, calificacion):
        return self.filter(reseñas__calificacion=calificacion)

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
    
    objects = LibrosManager()  # Asigna el gestor de consultas personalizado
    
    def __str__(self):
        return f"{self.titulo} - {self.descripcion}, {self.autores_id.nombre}"
    
    def promedio_calificaciones(self):
        promedio = self.reseñas.aggregate(avg_calificacion=Avg('calificacion'))['avg_calificacion']
        return promedio if promedio else 0.0
    
    
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
    calificacion_choice = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    calificacion= models.IntegerField(choices= calificacion_choice, null=False, blank=False)
    models.IntegerField(null=False, blank=False)
    comentario = models.TextField(max_length=500)
    fecha_reseña = models.DateTimeField(default=timezone.now)
    
    
        
    def __str__(self):
        return f"{self.comentario}, {self.calificacion}, {self.fecha_reseña}, {self.usuario_id.nombre}"
    

class ComentarioReseña(models.Model):
    comentario_id = models.AutoField(primary_key=True)
    reseña = models.ForeignKey('Reseñas', on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE, related_name='comentarios')
    comentario = models.TextField(max_length=300)
    fecha_comentario = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comentario de {self.usuario.nombre} en la reseña de {self.reseña.usuario_id.nombre}: {self.comentario}"
    
    

