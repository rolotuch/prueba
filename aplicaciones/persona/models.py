from django.db import models
from django.db.models.fields import CharField

from aplicaciones.departamento.models import Departamento

from ckeditor.fields import RichTextField


# Create your models here.
class Habilidades(models.Model):
    """modelo para la tabla habilidades
    Esto es una prueba
    """
    habilidad = models.CharField('Habilidad', max_length=50)


    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades empleado"
        
    def __str__(self):
        return str(self.id) + '-' + self.habilidad

class Empleado(models.Model):
    """modelo definido para la tabla empleado"""
    """LO QUE SE GURDA DE UN CHOICE EN LA BD ES EL INDICE NO EL NOMBRE """
    JOB_CHOICES = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro'),
    )
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField('nombre Completo', max_length = 120, blank= True)    
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    #avatar = models.ImageField(upload_to='empleado', blank=True, null= True)
    #relacionar emp0leado con habilidades
    habilidades = models.ManyToManyField(Habilidades)
    #     #image= models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)
    hoja_vida = RichTextField()

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Colaboradores"
        ordering = ['first_name']
        #este lo que hace es no dejar que se agregue otro departamento si ya tengo uno.
        #con el mismo nombre
        unique_together = ('first_name', 'last_name') #le indico que valide que no se registre una combinacion de nombre y nombre corto

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name
