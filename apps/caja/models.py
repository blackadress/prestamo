from django.db import models

# Create your models here.

class Caja(models.Model):
    nombre = models.CharField(max_length=30)
    monto = models.IntegerField()
    