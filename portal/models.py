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

class Reclamo(models.Model):
    nombre = models.CharField(max_length=100)
    cuerpo = models.TextField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    producto = models.CharField(max_length=100)
    descripcion = models.TextField()
    ofertar = models.IntegerField(default=None)
    fecha_publicacion = models.DateTimeField(default = timezone.now)
    usuario = models.ForeignKey(User, on_delete= models.CASCADE)

class Usuario(models.Model):
    rut =models.CharField(max_length=10, primary_key=True)
    nombre =models.CharField(max_length=50)
    apellido =models.CharField(max_length=50)