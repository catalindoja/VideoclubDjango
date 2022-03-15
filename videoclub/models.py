from django.db import models


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