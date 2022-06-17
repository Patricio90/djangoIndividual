from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm

def registro(request):
    if request.method =='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            usuario=form.cleaned_data.get('username')
            print(usuario)
    form = UserRegistrationForm()
    return render(request, 'user/register.html',{'form':form })
# Create your views here.
