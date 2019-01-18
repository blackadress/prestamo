from django.db import models

from apps.empleado.models import Empleado
from apps.cliente.models import Cliente
from apps.caja.models import Caja

# Create your models here.

class Prestamo(models.Model):
    ESTADOS_PRESTAMOS = (
        ('1', 'Creado'),
        ('2', 'Aprobado'),
        ('3', 'Salida de caja'),
        ('4', 'Por cobrar'),
        ('5', 'Cobrado')
    )
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now=True)
    montoPrestado = models.IntegerField()
    interes = models.IntegerField()
    montoPagado = models.IntegerField()
    plazo = models.DateTimeField()
    estado = models.CharField(choices=ESTADOS_PRESTAMOS, max_length=10, default='1')
    aprobado = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)
    supervisor = models.ForeignKey(Empleado, related_name='supervisor', on_delete=models.CASCADE)
    cajero = models.ForeignKey(Empleado, related_name='cajero', on_delete=models.CASCADE)
    caja = models.ForeignKey(Caja, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Cobro(models.Model):
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    cobrador = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
