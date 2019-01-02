from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombres = models.CharField(max_length=50)
    apPaterno = models.CharField(max_length=30)
    apMaterno = models.CharField(max_length=30)
    dni = models.CharField(max_length=8)
    activo = models.BooleanField(default=False)
    fechaIngreso = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now=True)
    latitud = models.CharField(max_length=25)
    longitud = models.CharField(max_length=25)