from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Videoclub
from .models import Pelicula
from .models import Cliente

def index(request):
    videoclubs = Videoclub.objects.all()
    #list_students = ", "\
    #   .join([student.name for student in students])
    #return HttpResponse(list_students)
    dictionary = {'videoclubs': videoclubs}
    return render(request, 'videoclub/index.html', dictionary)

def pelicula(request):
    peliculas = Pelicula.objects.all()
    # list_students = ", "\
    #   .join([student.name for student in students])
    # return HttpResponse(list_students)
    dictionary = {'peliculas': peliculas}
    return render(request, 'videoclub/pelicula.html', dictionary)

def cliente(request):
    cliente = Cliente.objects.all()
    # list_students = ", "\
    #   .join([student.name for student in students])
    # return HttpResponse(list_students)
    dictionary = {'clientes': cliente}
    return render(request, 'videoclub/cliente.html', dictionary)