from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Libros, Usuarios, Autores, Genero, Reseñas, ComentarioReseña


class UsuariosAdmin(UserAdmin):
    model = Usuarios
    list_display = ('email', 'nombre', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'nombre', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nombre', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


# Register your models here.
admin.site.register(Libros)
admin.site.register(Autores)
admin.site.register(Genero)
admin.site.register(Reseñas)
admin.site.register(ComentarioReseña)
# Registrar el modelo Usuarios con el administrador personalizado
admin.site.register(Usuarios, UsuariosAdmin)
