from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .models import Videoclub, Empleado, Pelicula, Cliente, Alquilado
from django.views.generic.edit import CreateView
from .forms import AlquiladoForm


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
    dictionary = {'alquilados': alquilado}
    return render(request, 'videoclub/lista_alquilados.html', dictionary)


def alquilar(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AlquiladoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # p = form.save()

            videoclub = form.cleaned_data['videoclub']
            pelicula = form.cleaned_data['pelicula']
            cliente = form.cleaned_data['cliente']
            empleado = form.cleaned_data['empleado']
            data = datetime.now()

            idalquiler = len(Alquilado.objects.all()) + 1

            alquilado = Alquilado(idalquiler, videoclub, empleado, cliente, pelicula, data)
            print(alquilado)
            alquilado.save()

            # redirect to a new URL:
            # if a GET (or any other method) we'll create a blank form
            return HttpResponseRedirect('lista_alquilados')
    else:
        form = AlquiladoForm()
    return render(request, "videoclub/alquilar_pelicula.html", {'form': form})


