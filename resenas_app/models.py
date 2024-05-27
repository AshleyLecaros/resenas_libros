from django.db import models
from django.utils import timezone
from django.db.models import Avg
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
import uuid

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
    

# Gestor de usuarios personalizado

class UsuariosManager(BaseUserManager):
    def create_user(self, email, nombre, password=None):
        if not email:
            raise ValueError('El email debe ser proporcionado')
        email = self.normalize_email(email)
        user = self.model(email=email, nombre=nombre)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nombre, password):
        user = self.create_user(email=email, nombre=nombre, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Usuarios(AbstractBaseUser, PermissionsMixin):
    usuarios_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=100, unique=True)
    tipo_usuario = models.CharField(max_length=50, default='Lector')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    password = models.CharField(max_length=128)

    objects = UsuariosManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

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
    
    
# Obtener el modelo de usuario personalizado
User = get_user_model()

# Modelo para gestionar el seguimiento de autores por parte de los usuarios
class SeguirAutor(models.Model):
    usuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE, related_name='seguimientos')
    autor = models.ForeignKey('Autores', on_delete=models.CASCADE, related_name='seguidores')
    fecha_seguimiento = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.usuario.nombre} sigue a {self.autor.nombre} desde {self.fecha_seguimiento}"
    

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()