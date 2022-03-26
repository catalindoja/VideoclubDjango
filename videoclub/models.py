from django.db import models
from datetime import date


# Create your models here.
class Videoclub(models.Model):
    idVideoclub = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60, blank=False, null=False)

    def __str__(self):
        return str(self.nombre)


class Empleado(models.Model):
    idEmpleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=False, null=False)
    apellidos = models.CharField(max_length=60, blank=False, null=False)
    idVideoclub = models.ForeignKey(Videoclub, default=1, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.nombre)


class Pelicula(models.Model):
    idPelicula = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60, blank=False, null=False)
    genero = models.CharField(max_length=60, blank=False, null=False)
    duracion = models.IntegerField(blank=False, null=False)
    fecha_de_lanzamiento = models.DateField(default=date.today)
    idVideoclub = models.ForeignKey(Videoclub, default=1, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.nombre)


class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=False, null=False)
    apellidos = models.CharField(max_length=60, blank=False, null=False)

    def __str__(self):
        return str(self.nombre)


class Alquilado(models.Model):
    idAlquiler = models.AutoField(primary_key=True)
    idVideoclub = models.ForeignKey(Videoclub, default=1, on_delete=models.PROTECT)
    idEmpleado = models.ForeignKey(Empleado, default=1, on_delete=models.PROTECT)
    idCliente = models.ForeignKey(Cliente, default=1, on_delete=models.PROTECT)
    idPelicula = models.ForeignKey(Pelicula, default=1, on_delete=models.PROTECT)
    fecha_de_alquiler = models.DateField(default=date.today)
