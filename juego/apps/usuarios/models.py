from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.partida.models import Pregunta

# Create your models here.

class Usuario(AbstractUser):
    puntaje = models.IntegerField(default = 0)
    
    pregunta_contestada = models.ManyToManyField(Pregunta)

    
