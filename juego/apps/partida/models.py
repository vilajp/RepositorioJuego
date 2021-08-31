from django.db import models
from apps.usuarios.models import Usuario

# Relaciones:
# Pregunta UNO-A-MUCHOS Respuesta -> ForeignKey va en MUCHOS

# Create your models here.

class Respuesta(models.Model):
    texto = models.CharField(max_length=200)
    es_correcta = models.BooleanField()

    pregunta = models.ForeignKey('Pregunta', on_delete = models.CASCADE)

    def __str__(self):
        return self.texto

class Pregunta(models.Model):
    texto = models.CharField(max_length=200)
    categoria = models.ForeignKey('Categoria', on_delete = models.CASCADE)

    def __str__(self):
        return self.texto

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Juego(models.Model):
    puntaje = models.IntegerField(default=0)
    cantidad_preguntas_contestadas = models.IntegerField(default=0)


    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)

class PreguntaContestada(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete = models.SET_NULL, null=True)
    correcta = models.BooleanField(default = False)
    pregunta = models.ForeignKey('Pregunta', on_delete = models.SET_NULL, null=True)
