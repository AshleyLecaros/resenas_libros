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
from resenas_app.views import index, registro_exitoso, registro_usuario, libros, detalle_libro, agregar_resena

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('registro_usuario', registro_usuario, name='registro_usuario'),
    path('registro_exitoso', registro_exitoso, name='registro_exitoso'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('libros/', libros, name='libros'),
    path('libros/<int:libro_id>/', detalle_libro, name='detalle_libro'),
    path('libros/<int:libro_id>/', agregar_resena, name='agregar_resena'),
    
    
    
]