from django import forms

class ContactForm(forms.Form):
    categoria=forms.ChoiceField(choices=[('pregunta','Pregunta'),('sugerencias','Sugerencias'),('otros','Otros')])
    nombre=forms.CharField()
    email=forms.EmailField(label='E-mail')
    Telefono=forms.IntegerField(label='Telefono')
    tema=forms.CharField(required=False)
    cuerpo=forms.CharField(widget=forms.Textarea)
