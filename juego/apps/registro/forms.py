from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.usuarios.models import Usuario


class RegistroFormulario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirma Contraseña', widget = forms.PasswordInput)

    class Meta:
        
       model = Usuario

       fields = [ 'username', 'email', 'password1', 'password2'   ]
        
       help_texts = {k:"" for k in fields}