from django.db import models

# Relaciones:
# Pregunta UNO-A-MUCHOS RespuestaIncorrecta -> ForeignKey va en MUCHOS
# Pregunta UNO-A-MUCHOS (o UNO-A-UNO) RespuestaCorrecta -> ForeignKey va en MUCHOS

from django.db import models

# Create your models here.
class RespuestaCorrecta(models.Model):
    texto = models.CharField(max_length=200)
    pregunta = models.ForeignKey('Pregunta', on_delete = models.CASCADE)
    #pregunta = models.ForeignKey('Pregunta', on_delete = models.SET_NULL, null=True)

    def __str__(self):
        return self.texto


class Pregunta(models.Model):
    texto = models.CharField(max_length=200)
    #respuesta_correcta = models.ForeignKey('RespuestaCorrecta',on_delete = models.CASCADE)
    categoria = models.ForeignKey('Categoria', on_delete = models.CASCADE)

    def __str__(self):
        return self.texto


class RespuestaIncorrecta(models.Model):
    texto = models.CharField(max_length=200)
    pregunta = models.ForeignKey('Pregunta', on_delete = models.CASCADE)
    #pregunta = models.ForeignKey('Pregunta', on_delete = models.SET_NULL, null=True)

    def __str__(self):
        return self.texto

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre