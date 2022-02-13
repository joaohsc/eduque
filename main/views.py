from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import UserRegisterForm

def index(request):
    return render(request, 'index.html')

def registro(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = form.cleaned_data.get('usuario')
            messages.success(request, f'{usuario}, sua conta foi criada com sucesso!') 
            return redirect('index')
    else:
        form = UserRegisterForm()

    context = {
        'form' : form,
    }

    return render(request, 'registro.html', context)

# def login(request):
#     if request.method == "POST":
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             usuario = form.cleaned_data.get('usuario')
#             messages.success(request, f'{usuario}, sua conta foi criada com sucesso!') 
#             return redirect('index')
#     else:
#         form = UserRegisterForm()

#     context = {
#         'form' : form,
#     }

#     return render(request, 'login.html', context)