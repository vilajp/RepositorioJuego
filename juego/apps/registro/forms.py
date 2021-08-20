from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.usuarios.models import Usuario


class RegistroFormulario(UserCreationForm):
    
    class Meta:
        model = Usuario

        fields = [

                'username',
                
            
                

        ]