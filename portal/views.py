from django.shortcuts import render
from django.http import HttpResponse

from portal.forms import ContactForm
from . models import Cliente

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def contacto(request):
    return render(request,'portal/contacto.html')

def clientes(request):
    cliente= Cliente.objects.all()
    return render(request, 'blog/clientes.html', {"data": cliente})

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
    return render(request,'blog/contacto.html',{'form':form})

# Create your views here.
