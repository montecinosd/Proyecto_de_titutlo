from django.forms import ModelForm
#from Registro_fullpega.models import *
from Publicar_trabajo.models import *

from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TrabajoForm(forms.ModelForm):
    class Meta:
        model = Trabajo
        fields = (['Nombre','Detalle','Monto_pago','Fecha','Hora','rango_etario','Area','Direccion'])
        # Fecha = forms.DateField(
        #     widget=forms.DateInput(format='%m/%d/%Y', attrs={'class': 'datepicker'}),
        #     input_formats=('%m/%d/%Y',)
        # )

        widgets = {'Nombre': forms.TextInput(attrs={'id':'Nombre','type':'text', 'class':'form-control','placeholder':'Ingrese nombre del trabajo'}),
                   'Detalle': forms.TextInput(attrs={'id':'Detalle','type':'text', 'class':'form-control','placeholder':'Ingrese detalle del trabajo'}),
                    'Fecha': forms.TextInput(attrs={'id':'Fecha','type':'date', 'class':'form-control','placeholder':'Ingrese la fecha del trabajo'}),
                   'Hora': forms.TextInput(attrs={'id': 'Hora', 'type': 'time', 'class': 'form-control','placeholder': 'Ingrese la hora del trabajo'}),
                   'Area': forms.TextInput(attrs={'id': 'Area', 'type': 'text', 'class': 'form-control',
                                                  'placeholder': 'Ingrese la area del trabajo'}),
                   'Direccion': forms.TextInput(attrs={'id': 'direccion', 'type': 'text', 'class': 'form-control',
                                                  'placeholder': 'Ingrese la dirección'}),

                   'rango_etario' : forms.Select(attrs={'class': 'form-control'}),
                   'Monto_pago': forms.TextInput(attrs={'id':'Monto_pago','type':'text', 'class':'form-control','placeholder':'Ingrese monto que esta dispuesto a pagar'}),}
