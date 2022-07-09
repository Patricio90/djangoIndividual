from unicodedata import name
from django.urls import path
from .import views
from .views import PublicacionDetalle, PublicacionCrear, PublicacionActualizar, PublicacionEliminar

urlpatterns = [
    path('', views.home, name ='portal-home'),
    path('about/', views.about, name ='about-portal'),
    path('clientes/', views.clientes, name= 'portal-clientes'),
    path('contacto/',views.contacto, name= 'portal-contacto'),
    path('reclamo/',views.reclamo),
    path('crearusuario/',views.crearUsuario),
    path('reclamo_detail/',views.reclamo_detail),
    path('catalogo/',views.catalogo, name ='portal-catalogo'),
    path('_publicacion/<int:pk>', PublicacionDetalle.as_view(), name = 'publicacion-detalle'),
    path('publicacion/new', PublicacionCrear.as_view(), name = 'publicacion-crear'),
    path('publicacion/<int:pk>/update/', PublicacionActualizar.as_view(), name = 'publicacion-actualizar'),
    path('publicacion/<int:pk>/delete/', PublicacionEliminar.as_view(), name = 'publicacion-elminar'),     
]

