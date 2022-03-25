from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Videoclub, Empleado


def index(request):
    videoclubs = Videoclub.objects.all()
    dictionary = {'videoclubs': videoclubs}
    return render(request, 'videoclub/index.html', dictionary)


def empleado(request):
    empleados = Empleado.objects.all()
    dictionary = {'empleados': empleados}
    return render(request, 'videoclub/empleados.html', dictionary)