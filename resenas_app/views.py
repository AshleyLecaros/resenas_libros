from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistroUsuarioForm, ReseñaForm
from django.contrib.auth.decorators import login_required
from .models import Libros, Reseñas


# Create your views here.

def index(request):
    return render(request, 'index.html')


def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libros.html')
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'registro_usuario.html', {'form': form})

def registro_exitoso(request):
    return render(request, 'registro_exitoso.html')


@login_required
def libros(request):
    nombre = request.user.username
    libros = Libros.objects.all()  # Obtén todos los libros

    context = {
        'nombre': nombre,
        'libros': libros,
    }
    return render(request, 'libros.html', context)


# Vista para el detalle del libro
def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libros, libros_id=libro_id)
    reseñas = libro.reseñas.all()
    context = {
        'libro': libro,
        'reseñas': reseñas
    }
    return render(request, 'detalle_libro.html', context)

def agregar_resena(request, libro_id):
    libro = get_object_or_404(Libros, libros_id=libro_id)

    if request.method == 'POST':
        form = ReseñaForm(request.POST)
        if form.is_valid():
            calificacion = form.cleaned_data['calificacion']
            comentario = form.cleaned_data['comentario']
            usuario = request.user  # Asumiendo que tienes un sistema de autenticación de usuario
            Reseñas.objects.create(libro=libro, usuario=usuario, calificacion=calificacion, comentario=comentario)
            return redirect('detalle_libro', libro_id=libro_id)
    else:
        form = ReseñaForm()

    return render(request, 'agregar_resena.html', {'form': form, 'libro': libro})



