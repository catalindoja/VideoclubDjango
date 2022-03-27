from django.shortcuts import render
from django.http import HttpResponse
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
    dictionary = {'alquilado': alquilado}
    return render(request, 'videoclub/lista_alquilados.html', dictionary)



def alquilar(request):
    context = {}
    context['form'] = AlquiladoForm()

    #template_name = "videoclub/alquilar_pelicula.html"
    def get(self,request):
        form = AlquiladoForm()
        return render(request, "videoclub/alquilar_pelicula.html", context)

    def post(self,request):
        form = AlquiladoForm(request.POST)
        if form.is_valid():
            videoclub = form.cleande_data['Videoclub']
            print(videoclub)
            print("")
            args = { 'form' : form, 'texthtml': videoclub}
            return render(request, self.template_name, context)
    return render(request, "videoclub/alquilar_pelicula.html", context)