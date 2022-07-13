from unicodedata import name
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name ='portal-home'),
    path('about/', views.about, name ='about-portal'),
    path('clientes/', views.clientes, name= 'portal-clientes'),
    path('contacto/',views.contacto, name= 'portal-contacto'),
    path('reclamo/',views.reclamo),
    path('crearusuario/',views.crearUsuario),
    path('reclamo_detail/',views.reclamo_detail),
    path('catalogo/',views.catalogo, name ='portal-catalogo'),
    path('agregar', views.agregarProducto, name='portal-agregar'),
    path('editar/<int:id>', views.editarProducto),
    path('eliminar/<int:id>', views.eliminarProducto),
    path('listar', views.listarProductos)     
]
#CRUD
