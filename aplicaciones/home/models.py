from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Prueba(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.titulo + ' ' + self.subtitulo