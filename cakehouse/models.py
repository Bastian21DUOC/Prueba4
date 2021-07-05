from django.db import models
from django.db.models.fields import IntegerField
from django.utils.translation import ugettext as _

# Create your models here.

class Sucursal(models.Model):
    nombre = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200, default='')
    fecha = models.DateTimeField("Fecha de elaboracion")
    precio = models.IntegerField(default=0)
    activo = models.BooleanField(default=False)

    def __str__(self):
        return self.descripcion

    class Meta:
        permissions = (
            ('Administrador',_('Es administrador')),

        )

class Usuario(models.Model):
    rut = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField(default=0)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)

    def __str__(self):
        return self.rut

