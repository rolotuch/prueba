from django.contrib import admin
from django.urls import path
from django.views.generic.base import View

from . import views

#para acceder a todo el conjunto de urls necesitamos agregar un nobre a todo este conjunto

app_name = "persona_app"

urlpatterns = [
    path('lempleado/', views.listAllEmpleados.as_view()),
    #shortname es un parametro que se le pasa a la vista en el metodo get_queryset
    path('empbyarea/<shortname>/', views.listByArea.as_view()),
    path('emp_clave/', views.ListEmpleadoByKword.as_view()),
    path('habilemp/', views.ListHabilidadesEmpleado.as_view()),
    #DETAILvies
    path('ver-empleado/<pk>', views.EmpleadoDtailView.as_view()),
    #createvies
    path('add-empleado/', views.EmpleadoCreateView.as_view()),
    
    #TemplateView    
    path('success/', views.successView.as_view(), name='Correcto'),    
    #UpdateView
    path('update-empleado/<pk>', views.EmpleadoUpdateView.as_view(), name='Update_empleado'),
]
