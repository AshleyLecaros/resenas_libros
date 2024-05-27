"""
URL configuration for resena_libros project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from resenas_app.views import index, registro_exitoso, registro_usuario, libros, detalle_libro, agregar_resena, actividades_usuario, seguir_autor, dejar_seguir, contact, agregar_libro, gestionar_autores, gestionar_usuarios, gestionar_reseñas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('registro_usuario/', registro_usuario, name='registro_usuario'),
    path('registro_exitoso', registro_exitoso, name='registro_exitoso'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('libros/', libros, name='libros'),
    path("contact/", contact, name='contact'),
    path('agregar_libro/', agregar_libro, name='agregar_libro'),
    path('gestionar_autores/', gestionar_autores, name='gestionar_autores'),
    path('gestionar_usuarios/', gestionar_usuarios, name='gestionar_usuarios'),
    path('gestionar_reseñas/', gestionar_reseñas, name='gestionar_reseñas'),
    path('libros/<int:libro_id>/', detalle_libro, name='detalle_libro'),
    path('libros/<int:libro_id>/agregar_resena/', agregar_resena, name='agregar_resena'),
    path('actividades/', actividades_usuario, name='actividades_usuario'),
    path('autor/<int:autor_id>/seguir/', seguir_autor, name='seguir_autor'),
    path('autor/<int:autor_id>/dejar_seguir/', dejar_seguir, name='dejar_seguir'),
    
    
    
]
