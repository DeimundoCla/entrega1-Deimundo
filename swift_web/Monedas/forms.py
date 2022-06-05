from django import forms
from django.forms import ModelForm
from matplotlib import widgets
from sympy import true
from .models import Dolar, Dolar_blue, Euro, Reais

#Formulario cotizaciones
class Usd_Form(ModelForm):
    class Meta:
        model = Dolar
        fields = ['nombre', 'cotizacion', 'fecha', 'variacion']
        
        widgets = {
            'nombre': forms.HiddenInput(attrs={'value': 'usd'}),
            'cotizacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cotización de la moneda',}),
            'fecha': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de la cotización', }),
            'variacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Variación de la cotización',}),
        }

class Usd_blue_Form(ModelForm):
    class Meta:
        model = Dolar_blue
        fields = ['nombre', 'cotizacion', 'fecha', 'variacion']
         
        widgets = {
            'nombre': forms.HiddenInput(attrs={'value': 'usd blue'}),
            'cotizacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cotización de la moneda',}),
            'fecha': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de la cotización', }),
            'variacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Variación de la cotización',}),
        }

class Euro_Form(ModelForm):
    class Meta:
        model = Euro
        fields = ['nombre', 'cotizacion', 'fecha', 'variacion']

        widgets = {
            'nombre': forms.HiddenInput(attrs={'value': 'euro'}),
            'cotizacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cotización de la moneda',}),
            'fecha': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de la cotización', }),
            'variacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Variación de la cotización',}),
        }
class Real_Form(ModelForm):
    class Meta:
        model = Reais
        fields = ['nombre', 'cotizacion', 'fecha', 'variacion']

        widgets = {
            'nombre': forms.HiddenInput(attrs={'value': 'real'}),
            'cotizacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cotización de la moneda',}),
            'fecha': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de la cotización', }),
            'variacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Variación de la cotización',}),
        }

class busqueda_Form(ModelForm):
    class Meta:
        model = Dolar
        fields = ['nombre', 'fecha']
        
        widgets = {
            'fecha': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de la cotización', }),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la moneda',}),        }
    class Meta:
        model = Dolar_blue
        fields = ['nombre', 'fecha']
        
        widgets = {
            'fecha': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de la cotización', }),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la moneda',}), 
        }
    class Meta:
        model = Euro
        fields = ['nombre', 'fecha']
        
        widgets = {
            'fecha': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de la cotización', }),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la moneda',}), 
        }
    class Meta:
        model = Reais
        fields = ['nombre', 'fecha']
        
        widgets = {
            'fecha': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de la cotización', }),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la moneda',}), 
        }