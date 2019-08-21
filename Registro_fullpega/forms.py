from django.forms import ModelForm
from Registro_fullpega.models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    username = forms.CharField(label='Ingrese su nombre',widget=forms.TextInput(attrs={'class':'form-control'}))
    # email = forms.EmailField(required=True,
    #                          label='Email',
    #                          error_messages={'exists': 'Oops'}, widget=forms.TextInput(attrs={'class':'form-control'}))

    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = (['username','password1', 'password2'])
        widgets = {'username': forms.TextInput(attrs={'id':'username','type':'text', 'class':'form-control','placeholder':'Ingrese nombre'}),
        'password1': forms.TextInput(attrs={'id':'password1','type':'text', 'class':'form-control','placeholder':'Ingrese su contraseña'}),
        'password2': forms.TextInput(attrs={'id':'password2','type':'text', 'class':'form-control','placeholder':'Ingrese su contraseña'}),}


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = (['Nombre','Fecha_nacimiento','Direccion','Rut'])
        widgets = {'Nombre': forms.TextInput(attrs={'id':'Rut','type':'text', 'class':'form-control','placeholder':'Ingrese su nombre'}),
                   'rut': forms.TextInput(attrs={'id':'Rut','type':'text', 'class':'form-control','placeholder':'Ingrese su rut'}),
                    'Fecha_nacimiento': forms.TextInput(attrs={'id':'Fecha_nacimiento','type':'text', 'class':'form-control','placeholder':'Ingrese fecha de nacimiento'}),
                    'Direccion': forms.TextInput(attrs={'id':'Direccion','type':'text', 'class':'form-control','placeholder':'Ingrese su direccion'}),}
