from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Empleado(models.Model):
    ROLES_OPCIONES = (
        ('cobrador', 'Cobrador'),
        ('cajero', 'Cajero'),
        ('supervisor', 'Supervisor'),
        ('administrador', 'Administrador')
    )

    nombres = models.CharField(max_length=50)
    apPaterno = models.CharField(max_length=30)
    apMaterno = models.CharField(max_length=30)
    dni = models.CharField(max_length=8)
    rol = models.CharField(max_length=15, choices=ROLES_OPCIONES)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)