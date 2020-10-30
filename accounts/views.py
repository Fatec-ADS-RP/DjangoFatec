from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy
from django.views import generic

from .forms import FormLogin, FormRegister, FormPasswordReset, FormPasswordConfirm

class PasswordConfirm(PasswordResetConfirmView):
    form_class = FormPasswordConfirm
    template_name = 'password/password_reset_confirm.html'

class PasswordReset(PasswordResetView):
    form_class = FormPasswordReset
    template_name = 'password/password_reset_form.html'

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

    else:
        form = FormLogin()

    return render(request, 'registration/login.html', {'form': form})

def cadastrar(request):
    context = {}
    if request.method == "POST":
        form = FormRegister(request.POST)
        if form.is_valid():
            form.save()
            context['is_valid'] = True
    else:
        form = FormRegister()

    context['form'] = form

    return render(request, 'registration/register.html', context)


