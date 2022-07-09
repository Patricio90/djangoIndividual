from django.contrib import admin
from . models import Cliente, Reclamo, Publicacion
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Reclamo)
admin.site.register(Publicacion)
