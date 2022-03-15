from django.db import models
from datetime import date

# Create your models here.

class Pelicula(models.Model):
     idPelicula = models.IntegerField(primary_key = True)
     nombre = models.TextField(blank=False, null=False)
     genero = models.TextField(blank=False, null=False)
     duracion = models.IntegerField(blank=False, null=False)
     fecha_de_lanzamiento = models.DateField(default=date.today)
     idVideoclub = models.ForeignKey(Videoclub, default=1, on_delete=models.PROTECT)

class Cliente(models.Model)
     idCliente = models.IntegerField(primary_key = True)
     nombre = models.TextField(blank=False, null=False)
     apellidos = models.TextField(blank=False, null=False)