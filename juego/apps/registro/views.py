from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import RegistroFormulario
 
from apps.usuarios.models import Usuario
# Create your views here.


class Create(CreateView):
    success_url = reverse_lazy('home')
    template_name = 'registro.html'
    model = Usuario
    form_class = RegistroFormulario

def form_valid(self,form):
    self.object = form.save(commit=False)
    self.object.set_password(self.object.password)
    self.object.save()
    return HttpResponseRedirect(self.get_success_url())