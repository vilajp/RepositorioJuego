from django.db import models

# Create your models here.
class Respuestas(models.Model):
    respuesta = models.CharField(max_length=200)
   
    def __str__(self):
        return self.respuesta


class Preguntas(models.Model):
    pregunta = models.CharField(max_length=200)
    respuesta_correcta = models.ForeignKey('Respuestas', related_name = 'mi_respuesta', on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return self.pregunta
    



