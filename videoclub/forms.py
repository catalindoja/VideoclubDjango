from django import forms
from .models import Alquilado, Videoclub, Empleado, Cliente, Pelicula


class AlquiladoForm(forms.Form):
    CHOICES_VIDEOCLUB = []
    CHOICES_PELICULA = []
    CHOICES_CLIENTE = []
    CHOICES_EMPLEADO = []

    for videoclub in Videoclub.objects.all():
        CHOICES_VIDEOCLUB.append((videoclub.idVideoclub, videoclub.nombre))

    for pelicula in Pelicula.objects.all():
        CHOICES_PELICULA.append((pelicula.idPelicula, pelicula.nombre))

    for cliente in Cliente.objects.all():
        CHOICES_CLIENTE.append((cliente.idCliente, cliente.nombre + " " + cliente.apellidos))

    for empleado in Empleado.objects.all():
        CHOICES_EMPLEADO.append((empleado.idEmpleado, empleado.nombre + " " + empleado.apellidos))

    videoclub = forms.CharField(label='Videoclub: ', widget=forms.Select(choices=CHOICES_VIDEOCLUB), required=False)
    empleado = forms.CharField(label='Empleado: ', widget=forms.Select(choices=CHOICES_EMPLEADO), required=False)
    cliente = forms.CharField(label='Cliente: ', widget=forms.Select(choices=CHOICES_CLIENTE), required=False)
    pelicula = forms.CharField(label='Pelicula: ', widget=forms.Select(choices=CHOICES_PELICULA), required=False)




