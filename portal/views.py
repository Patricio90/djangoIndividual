from django.shortcuts import render
from django.http import HttpResponse

from portal.forms import ContactForm
from . models import Cliente
from .forms import ReclamoForm, UsuariosForm

publicacion = [
          {
              'autor':'Felipe',
              'Titulo':'Venta',
              'Contenido':'Hola, vendo articulo en buen estado',
              'Fecha publicacion':'14-04-22'
          },
          {
              'autor':'Andrea',
              'Titulo':'Permuto',
              'Contenido':'Hola, vendo articulo en buen estado',
              'Fecha publicacion':'22-05-22'
          },
          {
              'autor':'Pedro',
              'Titulo':'Venta',
              'Contenido':'Hola, vendo articulo en buen estado',
              'Fecha publicacion':'05-03-22'
          }
]

def publicar(request):
    contexto ={
        'publicacion': publicacion
    }
    return render(request, 'portal/publicar.html', contexto)

def home(request):
    return render(request, 'portal/home.html')

def about(request):
    return render(request, 'portal/about.html')

# def contacto(request):
#     return render(request,'portal/contacto.html')

def clientes(request):
    cliente= Cliente.objects.all()
    return render(request, 'portal/clientes.html', {"data": cliente})

def reclamo(request):
    return render(request, 'portal/reclamo.html')

def catalogo(request):
    return render(request, 'portal/catalogo.html')

def contacto(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            nombre=form.cleaned_data["nombre"]
            email=form.cleaned_data["email"]
            Telefono=form.cleaned_data["Telefono"]
            cuerpo=form.cleaned_data["cuerpo"]
            print(nombre,email,Telefono,cuerpo)
    form=ContactForm()
    return render(request,'portal/contacto.html',{"form":form})

def reclamo_detail(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            cuerpo = form.cleaned_data["cuerpo"]
            print(nombre,cuerpo,"Funciona")
        form.save()
    form = ReclamoForm()
    return render(request,'portal/contacto.html',{'form':form})

def crearUsuario(request):
    #dinamico
    if request.method == "POST":
        form=UsuariosForm(data = request.POST)
        nombre=form.cleaned_data["nombre"]
        email=form.cleaned_data["email"]
        clave=form.cleaned_data["password"]
        user=user.objects.create_user(nombre,email,clave)
        user.save()
        return render(request,'portal/usuariocreado.html')
    form=UsuariosForm()
    return render(request,'portal/crearusuario.html',{"form":form})

# Create your views here.
