from django import forms
from portal.models import Reclamo
from django.db.models import fields
from .models import Producto

class ContactForm(forms.Form):
    categoria=forms.ChoiceField(choices=[('pregunta','Pregunta'),('sugerencias','Sugerencias'),('otros','Otros')])
    nombre=forms.CharField()
    email=forms.EmailField(label='E-mail')
    Telefono=forms.IntegerField(label='Telefono')
    tema=forms.CharField(required=False)
    cuerpo=forms.CharField(widget=forms.Textarea)

class ReclamoForm(forms.ModelForm):
    class Meta:
        model = Reclamo
        fields = {'nombre','cuerpo'}

class UsuariosForm(forms.Form):
    nombre=forms.CharField(widget=forms.TextInput)
    email=forms.CharField(widget=forms.EmailInput)
    password=forms.CharField(widget=forms.PasswordInput)

class FormProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields=('producto','descripcion','ofertar','fecha_publicacion','usuario')


              

