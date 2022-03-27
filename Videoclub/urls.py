""""Videoclub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import videoclub.views

urlpatterns = [
    path('', videoclub.views.index),
    path('videoclub/', include('videoclub.urls')),
    path('empleados', videoclub.views.empleado),
    path('clientes', videoclub.views.cliente),
    path('peliculas', videoclub.views.pelicula),
    path('lista_alquilados', videoclub.views.alquilado),
    path('alquilar_pelicula', videoclub.views.alquilar),
    path('admin/', admin.site.urls),
]
