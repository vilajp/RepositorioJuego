from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.usuarios.models import Usuario


class RegistroFormulario(UserCreationForm):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = Usuario

        fields = [

                'first_name',
                'last_name',
                

        ]