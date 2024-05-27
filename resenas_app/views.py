from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistroUsuarioForm, ReseñaForm, ComentarioReseñaForm
from django.contrib.auth.decorators import login_required
from .models import Libros, Reseñas, Usuarios, ComentarioReseña, Genero,Autores


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
