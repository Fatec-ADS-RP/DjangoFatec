from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic

from .forms import FormLogin, FormRegister

class Login(LoginView):
    form_class = FormLogin

def logar(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('website:index')
        else:
            form = FormLogin()
            print('Entrou')
    else:
        form = FormLogin()

    return render(request, 'registration/login.html', {'form': form})

def cadastrar(request):
    if request.method == "POST":
        form = FormRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/register_sucess')
    else:
        form = FormRegister()

    return render(request, 'registration/register.html', {'form': form})

def registerSucess(request):
    return render(request, 'registration/register_sucess.html')

