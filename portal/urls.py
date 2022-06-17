from unicodedata import name
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name ='portal-home'),
    path('about/', views.about, name ='about-portal'),
    path('clientes/', views.clientes, name= 'portal-clientes'),
    path('contacto/',views.contacto)    
]
