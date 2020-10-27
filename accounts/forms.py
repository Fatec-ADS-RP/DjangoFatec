from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.widgets import PasswordInput, TextInput


class FormLogin(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'validate','placeholder': 'Usuário'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'Senha'})
    )

class FormRegister(UserCreationForm):

    email = forms.EmailField(
        label="E-mail",
        widget=forms.TextInput(attrs={'autocomplete': 'email'}),
        help_text="Entre com um e-mail válido!",
    )

    first_name = forms.CharField(
        label="Primeiro Nome",
        widget=forms.TextInput(attrs={'autocomplete': 'first_name'}),
        help_text="Primeiro nome",
    )

    last_name = forms.CharField(
        label="Último Nome",
        widget=forms.TextInput(attrs={'autocomplete': 'last_name'}),
        help_text="Último nome",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'Usuário'})
        self.fields['first_name'].widget.attrs.update({'placeholder':'Primeiro Nome'})
        self.fields['last_name'].widget.attrs.update({'placeholder':'Último Nome'})
        self.fields['email'].widget.attrs.update({'placeholder':'Email'})
        self.fields['password1'].widget.attrs.update({'placeholder':'Senha'})        
        self.fields['password2'].widget.attrs.update({'placeholder':'Repetir Senha'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        error_messages = {
            'username': {
                'unique': 'Já existe no cadastro um usuário com este nome.',
            },
        }

