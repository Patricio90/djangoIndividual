from django.shortcuts import render, redirect
from django.http import HttpResponse
from portal.forms import ContactForm
from . models import Cliente
from .forms import ReclamoForm, UsuariosForm
from .forms import FormProducto
from .models import Producto
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'portal/home.html')

def about(request):
    return render(request, 'portal/about.html')

def publicar(request):
    return render(request,'portal/publicar.html')

# def contacto(request):
#     return render(request,'portal/contacto.html')

def clientes(request):
    cliente= Cliente.objects.all()
    return render(request, 'portal/clientes.html', {"data": cliente})

def reclamo(request):
    return render(request, 'portal/reclamo.html')

def catalogo(request):
    productos=Producto.objects.all()
    return render(request, 'portal/catalogo.html',{"productos": productos})

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
@login_required
def agregarProducto(request):
    form=FormProducto()
    if request.method == "POST":
        form=FormProducto(data = request.POST)
        producto= form.save(commit=False)
        producto.save()
        return redirect('/portal/listar')
    else:
        return render(request,'portal/crearProducto.html',{"form":form})

def eliminarProducto(request, id):
    producto= Producto.objects.get(pk=id)
    producto.delete()
    #return render(request,'portal/editarProducto.html')
    return redirect('/portal/listar')
        #return render(request,'portal/editarProducto.html',{"form":form})
    
    
def editarProducto(request , id):
    producto= Producto.objects.get(pk=id)
    #return render(request,'portal/editarProducto.html')
    form=FormProducto(instance=producto)
    if request.method == "POST":
        #editar
        form=FormProducto(data=request.POST, instance=producto)
        form.save()
        producto= form.save(commit=False)
        producto.save()
        return redirect('/portal/listar')
        #return render(request,'portal/editarProducto.html',{"form":form})
    else:
        return render(request,'portal/editarProducto.html',{"form":form})

def listarProductos(request):
    productos=Producto.objects.all()
    return render(request, 'portal/catalogo.html',{"productos": productos})
    


    

    



# Create your views here.
