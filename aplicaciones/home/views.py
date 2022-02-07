from django.shortcuts import render

from django.views.generic import (
     TemplateView, ListView, CreateView
)
from .models import Prueba

# Create your views here.
class pruebaView(TemplateView):
    template_name = 'home/prueba.html'


# class pruebaListView(ListView):
#     queryset = ['1','10','20','30']
#     template_name = "home/list.html"
#     context_object_name = 'listanumeros'


class PruebaView(ListView):
    template_name = "home/lista_prueba.html"
    model = Prueba
    context_object_name = 'lista'


class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    fields = ['titulo', 'subtitulo', 'cantidad']