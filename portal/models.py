from django.db import models
from django import forms

# Create your models here.
class Cliente(models.Model):
    rut=models.CharField(max_length=10, unique=True)
    nombre=models.CharField(max_length=50, default=None)
    apellido=models.CharField(max_length=100, default=None)
    edad = models.IntegerField(default=None)
    direccion=models.CharField(max_length=100, default=None)
    correo=models.CharField(max_length=50, default=None)

class Reclamo(models.Model):
    nombre = models.CharField(max_length=100)
    cuerpo = models.TextField()

    def __str__(self):
        return self.nombre