from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Videoclub, Empleado, Pelicula, Cliente, Alquilado


def index(request):
    videoclubs = Videoclub.objects.all()
    dictionary = {'videoclubs': videoclubs}
    return render(request, 'videoclub/index.html', dictionary)


def empleado(request):
    empleados = Empleado.objects.all()
    dictionary = {'empleados': empleados}
    return render(request, 'videoclub/empleados.html', dictionary)

def pelicula(request):
    peliculas = Pelicula.objects.all()
    dictionary = {'peliculas': peliculas}
    return render(request, 'videoclub/pelicula.html', dictionary)

def cliente(request):
    cliente = Cliente.objects.all()
    dictionary = {'clientes': cliente}
    return render(request, 'videoclub/cliente.html', dictionary)

def alquilado(request):
    alquilado = Alquilado.objects.all()
    dictionary = {'clientes': cliente}
    return render(request, 'videoclub/lista_alquilados.html', dictionary)
