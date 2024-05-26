from django import forms
from .models import Usuarios, Reseñas

class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombre', 'email', 'password']

    password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuarios.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email ya está registrado.')
        return email
    
class ReseñaForm(forms.ModelForm):
    class Meta:
        model = Reseñas
        fields = ['calificacion', 'comentario']
        labels = {
            'calificacion': 'Calificación',
            'comentario': 'Comentario',
        }