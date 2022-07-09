from django.shortcuts import render
from django.http import HttpResponse
from portal.forms import ContactForm
from .models import Cliente
from .models import Publicacion
from .forms import ReclamoForm, UsuariosForm
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    return render(request, 'portal/home.html')

def publicar(request):
    contexto = {
        'posts' : Publicacion.objects.all()
    }
    return render(request,'portal/publicar.html', contexto)

def about(request):
    return render(request, 'portal/about.html')

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

#vistas

class PublicacionDetalle(DetailView):
    model = Publicacion
    template_name ='portal/publicacion_detalle.html'

class PublicacionCrear(LoginRequiredMixin, CreateView):
    model = Publicacion
    fields=['fecha_publicacion','producto','descripcion','ofertar','ofertado_por']

    def form_valid(self, form):
        form.instance.ofertado_por = self.request.user
        return super().form_valid(form)

class PublicacionActualizar(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Publicacion
    fields=['fecha_publicacion','producto','descripcion','ofertar','ofertado_por']

    def test_func(self):
        publicacion  = self.get_object()
        if self.request.user == publicacion.ofertado_por:
            return True
        return False

class PublicacionEliminar(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Publicacion
    template_name ='portal/publicacion_eliminar.html'
    success_url = 'about/'
    def test_func(self):
        publicacion  = self.get_object()
        if self.request.user == publicacion.ofertado_por:
            return True
        return False