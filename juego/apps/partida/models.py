from django.db import models

# Create your models here.
class Respuestas(models.Model):
    respuesta = models.CharField(max_length=200)
   
    def __str__(self):
        return self.respuesta


class Preguntas(models.Model):
    pregunta = models.CharField(max_length=200)
    respuesta_correcta = models.ForeignKey('Respuestas', related_name = 'mi_respuesta', on_delete = models.SET_NULL, null = True)
    respuesta_erronea = models.ForeignKey('Respuesta_Incorrecta', related_name = 'mi_respuesta_inc', on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return self.pregunta
    

class Respuesta_Incorrecta(models.Model):
    respuesta_incorrecta = models.CharField(max_length=200)

    def __str__(self):
        return self.respuesta_incorrecta

    