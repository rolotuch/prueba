from django.contrib import admin
from django.urls import path, re_path, include
#con punto digo qeu el archivo que busco esta en el mismo nivel que este archivo.
from . import views


urlpatterns = [
    path('prueba/', views.pruebaView.as_view()),
    #path('lista/', views.pruebaListView.as_view()),
    path('lista2/', views.PruebaView.as_view()),
     path('crear/', views.PruebaCreateView.as_view()),
       
]
