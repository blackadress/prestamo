from django.db import models

from apps.empleado.models import Empleado
from apps.cliente.models import Cliente

# Create your models here.

class Ruta(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField()
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    clientes = models.ManyToManyField(Cliente)