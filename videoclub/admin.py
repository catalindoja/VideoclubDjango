from django.contrib import admin
from videoclub import models

# Register your models here.
admin.site.register(models.Videoclub)
admin.site.register(models.Pelicula)
admin.site.register(models.Cliente)
admin.site.register(models.Empleado)
admin.site.register(models.Alquilado)