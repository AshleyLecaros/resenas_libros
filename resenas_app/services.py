from django.core.exceptions import ObjectDoesNotExist
from .models import Usuarios, Libros, Reseñas

# CRUD para Usuarios
def crear_usuario(nombre, email, password, tipo_usuario='Lector', is_active=True, is_staff=False):
    usuario = Usuarios.objects.create(
        nombre=nombre,
        email=email,
        tipo_usuario=tipo_usuario,
        is_active=is_active,
        is_staff=is_staff
    )
    usuario.set_password(password)
    usuario.save()
    return usuario

def mostrar_usuario(usuario_id):
    try:
        return Usuarios.objects.get(pk=usuario_id)
    except ObjectDoesNotExist:
        return None

def actualizar_usuario(usuario_id, nombre=None, email=None, password=None, tipo_usuario=None, is_active=None, is_staff=None):
    try:
        usuario = Usuarios.objects.get(pk=usuario_id)
        if nombre:
            usuario.nombre = nombre
        if email:
            usuario.email = email
        if password:
            usuario.set_password(password)
        if tipo_usuario:
            usuario.tipo_usuario = tipo_usuario
        if is_active is not None:
            usuario.is_active = is_active
        if is_staff is not None:
            usuario.is_staff = is_staff
        usuario.save()
        return usuario
    except ObjectDoesNotExist:
        return None

def eliminar_usuario(usuario_id):
    try:
        usuario = Usuarios.objects.get(pk=usuario_id)
        usuario.delete()
        return True
    except ObjectDoesNotExist:
        return False

# CRUD para Libros
def crear_libro(titulo, descripcion, año_publicacion, portada_url, genero_id, autores_id):
    libro = Libros.objects.create(
        titulo=titulo,
        descripcion=descripcion,
        año_publicacion=año_publicacion,
        portada_url=portada_url,
        genero_id=genero_id,
        autores_id=autores_id
    )
    libro.save()
    return libro

def mostrar_libro(libro_id):
    try:
        return Libros.objects.get(pk=libro_id)
    except ObjectDoesNotExist:
        return None

def actualizar_libro(libro_id, titulo=None, descripcion=None, año_publicacion=None, portada_url=None, genero_id=None, autores_id=None):
    try:
        libro = Libros.objects.get(pk=libro_id)
        if titulo:
            libro.titulo = titulo
        if descripcion:
            libro.descripcion = descripcion
        if año_publicacion:
            libro.año_publicacion = año_publicacion
        if portada_url:
            libro.portada_url = portada_url
        if genero_id:
            libro.genero_id = genero_id
        if autores_id:
            libro.autores_id = autores_id
        libro.save()
        return libro
    except ObjectDoesNotExist:
        return None

def eliminar_libro(libro_id):
    try:
        libro = Libros.objects.get(pk=libro_id)
        libro.delete()
        return True
    except ObjectDoesNotExist:
        return False

# CRUD para Reseñas
def crear_reseña(libro_id, usuario_id, calificacion, comentario):
    reseña = Reseñas.objects.create(
        libro_id=libro_id,
        usuario_id=usuario_id,
        calificacion=calificacion,
        comentario=comentario
    )
    reseña.save()
    return reseña

def mostrar_reseña(reseña_id):
    try:
        return Reseñas.objects.get(pk=reseña_id)
    except ObjectDoesNotExist:
        return None

def actualizar_reseña(reseña_id, calificacion=None, comentario=None):
    try:
        reseña = Reseñas.objects.get(pk=reseña_id)
        if calificacion:
            reseña.calificacion = calificacion
        if comentario:
            reseña.comentario = comentario
        reseña.save()
        return reseña
    except ObjectDoesNotExist:
        return None

def eliminar_reseña(reseña_id):
    try:
        reseña = Reseñas.objects.get(pk=reseña_id)
        reseña.delete()
        return True
    except ObjectDoesNotExist:
        return False
