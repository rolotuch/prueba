from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    shortname = models.CharField('Nombre corto', max_length=20, unique=True)    
    anulate = models.BooleanField('Anulado', default=False)

    #este clase es como un decorador
    class Meta:
        verbose_name = "mi departamento"
        verbose_name_plural = "Areas de la empresa"
        ordering = ['name']
        #este lo que hace es no dejar que se agregue otro departamento si ya tengo uno.
        #con el mismo nombre
        unique_together = ('name', 'shortname') #le indico que valide que no se registre una combinacion de nombre y nombre corto
        
    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.shortname
