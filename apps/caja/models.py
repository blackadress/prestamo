from django.db import models

# Create your models here.

class Caja(models.Model):
    nombre = models.CharField(max_length=30)
    fecha = models.DateTimeField(auto_now_add=True)
    saldo = models.IntegerField()
    activo = models.BooleanField(default=True)
    