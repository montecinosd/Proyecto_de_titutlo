from django.forms import ModelForm
#from Registro_fullpega.models import *
from Publicar_trabajo.models import *

from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TrabajoForm(forms.ModelForm):
    class Meta:
        model = Trabajo
        fields = (['Nombre','Detalle','Monto_pago','Fecha'])
        # Fecha = forms.DateField(
        #     widget=forms.DateInput(format='%m/%d/%Y', attrs={'class': 'datepicker'}),
        #     input_formats=('%m/%d/%Y',)
        # )
        widgets = {'Nombre': forms.TextInput(attrs={'id':'Rut','type':'text', 'class':'form-control','placeholder':'Ingrese nombre del trabajo'}),
                   'Detalle': forms.TextInput(attrs={'id':'Rut','type':'text', 'class':'form-control','placeholder':'Ingrese detalle del trabajo'}),
                    'Fecha': forms.TextInput(attrs={'id':'Rut','type':'date', 'class':'form-control','placeholder':'Ingrese detalle del trabajo'}),
                    'Monto_pago': forms.TextInput(attrs={'id':'Direccion','type':'text', 'class':'form-control','placeholder':'Ingrese monto que esta dispuesto a pagar'}),}
