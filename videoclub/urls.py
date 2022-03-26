from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('videoclub', views.index),
    path('empleados', views.empleado),
    path('peliculas', views.pelicula),
    path('clientes', views.cliente),
]
