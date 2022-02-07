from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.
class HabilidadAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'habilidad',
    )
    search_fields = ('habilidad',)
    
admin.site.register(Habilidades, HabilidadAdmin)

#decoradores para cambiar la apariencia en el admin
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
    )
    #el field full_name no existe enb la tabla asi que para que aparezca debo realizar una funcion
    def full_name(self, obj):
        #toda la operacion
        #print (obj.first_name + obj.last_name)
        return obj.first_name + " " + obj.last_name

    search_fields = ('first_name',)
    list_filter = ('job', )
    #filtro horizontal solo funciona con las relaciones muchos a muchos
    filter_horizontal = ('habilidades',)
    

admin.site.register(Empleado, EmpleadoAdmin)