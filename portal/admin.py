from django.contrib import admin
from . models import Cliente, Reclamo, Producto
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Reclamo)
admin.site.register(Producto)
