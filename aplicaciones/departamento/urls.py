from django.contrib import admin
from django.urls import path



def depto(self):
    print("prueba depto")


urlpatterns = [
    path('departamento/', depto),
]
