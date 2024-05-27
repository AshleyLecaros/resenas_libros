from django import forms
from .models import Usuarios, Reseñas, ComentarioReseña, Libros, Autores

class RegistroUsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuarios
        fields = ['nombre', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuarios.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email ya está registrado.')
        return email

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data['password'])
        if commit:
            usuario.save()
        return usuario
    
class ReseñaForm(forms.ModelForm):
    class Meta:
        model = Reseñas
        fields = ['calificacion', 'comentario']
        
        
class ComentarioReseñaForm(forms.ModelForm):
    class Meta:
        model = ComentarioReseña
        fields = ['comentario']
        

class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label="Correo")
    customer_name = forms.CharField(max_length=64, label="Nombre")
    message = forms.CharField(label="Mensaje")
    
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libros
        fields = ['titulo', 'descripcion', 'año_publicacion', 'portada_url', 'genero_id', 'autores_id']
        
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autores
        fields = ['nombre']
        
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombre', 'email', 'password', 'tipo_usuario', 'is_active', 'is_staff']
        widgets = {
            'password': forms.PasswordInput(),
        }


