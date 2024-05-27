from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistroUsuarioForm, ReseñaForm, ComentarioReseñaForm, ContactFormForm, LibroForm, AutorForm, UsuarioForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from .models import Libros, Reseñas, Usuarios, ComentarioReseña, Genero,Autores, SeguirAutor, ContactForm


# Create your views here.

def index(request):
    return render(request, 'index.html')


def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro_exitoso') 
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'registro_usuario.html', {'form': form})

def registro_exitoso(request):
    return render(request, 'registro_exitoso.html')


@login_required
def libros(request):
    nombre = request.user.nombre
    
    # Obtén todos los libros
    libros = Libros.objects.all()
    
    # Obtén todos los géneros y autores
    generos = Genero.objects.all()
    autores = Autores.objects.all()
    
    # Filtrar por categoría
    genero_id = request.GET.get('genero')
    if genero_id:
        libros = Libros.objects.filter(genero_id=genero_id)
    
    # Filtrar por autor
    autor_id = request.GET.get('autor')
    if autor_id:
        libros = Libros.objects.filter(autores_id=autor_id)
    
    # Filtrar por calificación
    calificacion = request.GET.get('calificacion')
    if calificacion:
        libros = Libros.objects.filter(reseñas__calificacion=calificacion)
    
    context = {
        'nombre': nombre,
        'libros': libros,
        'generos': generos,
        'autores': autores,
    }
    return render(request, 'libros.html', context)


# Vista para el detalle del libro
@login_required
def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libros, libros_id=libro_id)
    reseñas = Reseñas.objects.filter(libro_id=libro)
    promedio_calificaciones = libro.promedio_calificaciones()

    # Formulario de comentario vacío para cada reseña
    comentario_form = ComentarioReseñaForm()

    if request.method == 'POST':
        form = ComentarioReseñaForm(request.POST)
        if form.is_valid():
            comentario = form.cleaned_data['comentario']
            usuario = request.user  # Usar el usuario autenticado
            usuario = Usuarios.objects.get(pk=request.user.pk)  # Obtener el usuario actual
            reseña_id = request.POST.get('reseña_id')
            reseña = get_object_or_404(Reseñas, reseña_id=reseña_id)
            ComentarioReseña.objects.create(reseña=reseña, usuario=usuario, comentario=comentario)
            return redirect('detalle_libro', libro_id=libro_id)
    else:
        form = ComentarioReseñaForm()

    context = {
        'libro': libro,
        'reseñas': reseñas,
        'form': comentario_form,
        'promedio_calificaciones': promedio_calificaciones,
    }
    return render(request, 'detalle_libro.html', context)

@login_required
def agregar_resena(request, libro_id):
    libro = get_object_or_404(Libros, libros_id=libro_id)

    if request.method == 'POST':
        form = ReseñaForm(request.POST)
        if form.is_valid():
            calificacion = form.cleaned_data['calificacion']
            comentario = form.cleaned_data['comentario']
            usuario = request.user  # Usar el usuario autenticado
            Reseñas.objects.create(libro_id=libro, usuario_id=usuario, calificacion=calificacion, comentario=comentario)
            return redirect('detalle_libro', libro_id=libro_id)
    else:
        form = ReseñaForm()

    context = {
        
        'libro': libro,
        'form': form,
    }
    return render(request, 'agregar_resena.html', context)

@login_required
def actividades_usuario(request):
    if request.user.is_authenticated:
        # Obtener el usuario autenticado
        usuario = get_object_or_404(Usuarios, usuarios_id=request.user.usuarios_id)

        # Obtener las reseñas y comentarios del usuario
        reseñas_usuario = Reseñas.objects.filter(usuario_id=usuario)
        comentarios_usuario = ComentarioReseña.objects.filter(usuario=usuario)
    else:
        usuario = None
        reseñas_usuario = []
        comentarios_usuario = []

    # Renderizar la plantilla con el contexto
    return render(request, 'actividades_usuario.html', {
        'usuario': usuario,
        'reseñas_usuario': reseñas_usuario,
        'comentarios_usuario': comentarios_usuario
    })

@login_required  
def seguir_autor(request, autor_id):
    autor = get_object_or_404(Autores, pk=autor_id)
    SeguirAutor.objects.get_or_create(Usuarios, usuario_id=request.user.usuarios_id, autor=autor)
    messages.success(request, f'Has comenzado a seguir a {autor.nombre}.') # Añadir un mensaje de éxito al contexto de la solicitud.
    return redirect('detalle_autor', autor_id=autor.id)

@login_required  
def dejar_seguir(request, autor_id):
    autor = get_object_or_404(Autores, pk=autor_id)
    SeguirAutor.objects.filter(Usuarios=request.user.usuario_id, autor=autor).delete() # Eliminar el registro de seguimiento si existe.
    messages.success(request, f'Has dejado de seguir a {autor_id.nombre}.')
    
    return redirect('detalle_autor', autor_id=autor.id)

def contact(request):
    if request.method == "POST":
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect("index")
    else:
        form = ContactFormForm()
    return render(request, "contact.html", {"form": form})

@user_passes_test(lambda u: u.is_superuser)
def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libros') 
    else:
        form = LibroForm()
    return render(request, 'agregar_libro.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def gestionar_autores(request):
    autores = Autores.objects.all()
    form_autor = AutorForm()

    if request.method == 'POST':
        form_autor = AutorForm(request.POST)
        if form_autor.is_valid():
            form_autor.save()
            return redirect('gestionar_autores')

    context = {
        "form_autor": form_autor,
        "autores": autores,
    }

    return render(request, 'gestionar_autores.html', context)

@user_passes_test(lambda u: u.is_superuser)
def gestionar_usuarios(request):
    usuarios = Usuarios.objects.all()
    form_usuario = UsuarioForm()

    if request.method == 'POST':
        form_usuario = UsuarioForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('gestionar_usuarios')

    context = {
        "form_usuario": form_usuario,
        "usuarios": usuarios,
    }

    return render(request, 'gestionar_usuarios.html', context)

@user_passes_test(lambda u: u.is_superuser)
def gestionar_reseñas(request):
    reseñas = Reseñas.objects.all()
    form_reseña = ReseñaForm()
    form_comentario = ComentarioReseñaForm()

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'add_reseña':
            form_reseña = ReseñaForm(request.POST)
            if form_reseña.is_valid():
                form_reseña.save()
                return redirect('gestionar_reseñas')

        elif action == 'add_comentario':
            form_comentario = ComentarioReseñaForm(request.POST)
            if form_comentario.is_valid():
                form_comentario.save()
                return redirect('gestionar_reseñas')

    context = {
        "form_reseña": form_reseña,
        "form_comentario": form_comentario,
        "reseñas": reseñas,
    }

    return render(request, 'gestionar_reseñas.html', context)
   