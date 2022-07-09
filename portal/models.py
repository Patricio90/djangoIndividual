from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Cliente(models.Model):
    rut=models.CharField(max_length=10, unique=True)
    nombre=models.CharField(max_length=50, default=None)
    apellido=models.CharField(max_length=100, default=None)
    edad = models.IntegerField(default=None)
    direccion=models.CharField(max_length=100, default=None)
    correo=models.CharField(max_length=50, default=None)

class Publicacion(models.Model):
        producto = models.CharField(max_length=100)
        descripcion = models.TextField()
        ofertar = models.IntegerField(default=None)
        fecha_publicacion = models.DateTimeField(default = timezone.now)
        ofertado_por = models.ForeignKey(User, on_delete= models.CASCADE)

        def __str__(self):
            return self.producto
        def get_absolute_url(self):
            return reverse('publicacion-detalle', kwargs = {'pk': self.pk} )

class Reclamo(models.Model):
    nombre = models.CharField(max_length=100)
    cuerpo = models.TextField()

    def __str__(self):
        return self.nombre