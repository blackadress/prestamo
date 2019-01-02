from django.db import models

from apps.empleado.models import Empleado
from apps.cliente.models import Cliente
from apps.caja.models import Caja

# Create your models here.

class Prestamo(models.Model):
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now=True)
    monto = models.IntegerField()
    estado = models.IntegerField(default=1)
    aprobado = models.BooleanField(default=False)
    supervisor = models.ForeignKey(Empleado, related_name='supervisor', on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, related_name='empleado', on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    caja = models.ForeignKey(Caja, on_delete=models.CASCADE)

class Cobro(models.Model):
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    cobrador = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
