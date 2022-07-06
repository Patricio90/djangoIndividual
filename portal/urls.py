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
    path('publicar/',views.publicar, name ='portal-publicar'),
    path('catalogo/',views.catalogo, name ='portal-catalogo')     
]

