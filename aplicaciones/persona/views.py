from django.views.generic.list import MultipleObjectTemplateResponseMixin
from aplicaciones.departamento.models import Departamento
from django.shortcuts import render

from django.urls import reverse_lazy

#viwes
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView)

#models
from .models import Empleado

# Create your views here.

#listar todos los empleados de la empresa
class listAllEmpleados(ListView):
    """lista todos los empleados"""
    template_name = "persona/list_all.html"
    #haremos una paginación para ver como ser realiza el metodo de paginacion
    paginate_by = 4
    #p_num = self.request.GET.get("kword",'')
    model = Empleado
    
#listar todos los empleados que pertenecen a un area de la empresa
class listByArea(ListView):
    #usamos el queryset envez del modelo para trabajar con varios tablas
    """ queryset = Empleado.objects.filter(
        departamento__shortname = 'otro',
    )
    """
    template_name = "persona/lbyarea.html"
    
    #lo anterior es la peor manera de ralizar un queryset, veamos cual es la MultipleObjectTemplateResponseMixin
    def get_queryset(self):
        #en la variable area recuperamos el parametro shortname qeu le emos enviado en la url
        #con el metodo sefl.kwargs recuperamos todos los parametros qaue vienen de esa url
        area = self.kwargs['shortname']
        lista = Empleado.objects.filter(
            departamento__shortname = area #en vez de definir el area de la empresa le pasamos el valor qaue tiene area. lo que recuperamos en la url
        )
        return lista

#listar empelaos por palabra clave
class ListEmpleadoByKword(ListView):
    """lista de empleados por palabra clave """
    template_name = "persona/bykword.html"
    context_object_name = 'empleados'

    def get_queryset(self):
        # variable para recoger la palabra que enviamos desde el form. con la instruccion request.GET le digo que me traiga todas
        # las solicitudes a servidor de tipo GET, cuyo identificador sea el kword, que es lo que le pusimos en el form en el html
        p_clave = self.request.GET.get("kword",'')
        #una vez que lo tengo lo puedo colocar en una lista como en el metodo anterior
        lista = Empleado.objects.filter(
            first_name = p_clave #en vez de definir el area de la empresa le pasamos el valor qaue tiene area. lo que recuperamos en la url
        )        
        return lista
        

#listar habilidades de empleados.
class ListHabilidadesEmpleado(ListView):
    template_name = "persona/habilidades.html"
    context_object_name = 'habilidades'

    def get_queryset(self):
        #aca le indicamos de cual empleado queremos traer las habilidades
        #en este caso por el empleado con el id numero 5, para hacerlo mas dinamos se puede utilizar la caja de texto del ejemplo mas arriba
        empleado = Empleado.objects.get(id=3)
        #con el metodo empleado.habilidades.all() es donde obtenemos todos las habilidades d eun empleado.
        #print(empleado.habilidades.all())

        return empleado.habilidades.all()

#listar empleados por trabajo


class EmpleadoDtailView(DetailView):
    model =Empleado
    template_name = "persona/detail_empleado.html"
    # tambien existe el metodo get veamos com utilizarlo
    def get_context_data (self, **kwargs):
        context = super(EmpleadoDtailView, self).get_context_data(**kwargs)
        context['titulo'] = 'empleado del mes'
        return context


#creamos un template para redireccionar a una pagina cuando se ingresa un registro, para el create view
class successView(TemplateView):
    template_name = "persona/success.html"


#Create View
class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    #fields =  ['first_name', 'last_name', 'job', 'departamento', 'habilidades', 'hoja_vida']
    #fields =  ['first_name', 'last_name', 'job']
    #fields =  ('__all__') #modificamos este para indicarle solo los parametros que necesitamos
    fields =  ['first_name', 'last_name', 'job', 'departamento', 'habilidades', 'hoja_vida']
    #aca le especificamos la url a la que queramos reenviar
    #success_url = '.' #esto es para indicarle que se quede en la misma pagina
    #success_url = '/success' otra forma
    success_url = reverse_lazy('persona_app:Correcto')
    #entonces estos son los cuatro parametros que necesita el create view

    def form_valid (self, form):
        #logica del proceso
        empleado = form.save(commite = False)
        #vemos si los esta guardando
        #print (empleado)
        empleado.full_name = empleado.first_name + ' '+ empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    template_name = "pesona/update.html"
    model = Empleado
    
