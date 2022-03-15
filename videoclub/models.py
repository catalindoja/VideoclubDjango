from django.db import models
from datetime import date


# Create your models here.
class Videoclub(models.Model):
    idVideoclub = models.IntegerField(primary_key=True)
    nombre = models.TextField(null=False, blank=False)

    def __unicode__(self):
        return u"%s" % self.nombre


class Empleado(models.Model):
    idEmpleado = models.IntegerField(primary_key=True)
    nombre = models.TextField(null=False, blank=False)
    apellido = models.TextField(null=False, blank=False)
    idVideoclub = models.ForeignKey(Videoclub, default=1, on_delete=models.PROTECT)

    def __unicode__(self):
        return u"%s" % self.nombre


class Pelicula(models.Model):
    idPelicula = models.IntegerField(primary_key=True)
    nombre = models.TextField(blank=False, null=False)
    genero = models.TextField(blank=False, null=False)
    duracion = models.IntegerField(blank=False, null=False)
    fecha_de_lanzamiento = models.DateField(default=date.today)
    idVideoclub = models.ForeignKey(Videoclub, default=1, on_delete=models.PROTECT)

    def __unicode__(self):
        return u"%s" % self.nombre


class Cliente(models.Model)
    idCliente = models.IntegerField(primary_key=True)
    nombre = models.TextField(blank=False, null=False)
    apellidos = models.TextField(blank=False, null=False)

    def __unicode__(self):
        return u"%s" % self.nombre