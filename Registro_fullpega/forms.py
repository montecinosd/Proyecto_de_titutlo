from django.forms import ModelForm
from Registro_fullpega.models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(ModelForm):
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','password1', 'password2', )

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields =['Nombre','Fecha_nacimiento','Email','Direccion','rut','dv','usuario']
