from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Dolar, Dolar_blue, Euro, Reais

# Create your views here.

def cotizacion_dolar(request):
    dolar = Dolar.objects.all()
    dicc = {'dolar': dolar}
    template = loader.get_template("dolar.html")
    documento = template.render(dicc)
    return HttpResponse(documento)

def cotizacion_euro(request):
    euro = Euro.objects.all()
    dicc = {'euro': euro}
    template = loader.get_template("euro.html")
    documento = template.render(dicc)
    return HttpResponse(documento)

def cotizacion_dolar_blue(request):
    dolar_blue = Dolar_blue.objects.all()
    dicc = {'dolar_blue': dolar_blue}
    template = loader.get_template("dolar_blue.html")
    documento = template.render(dicc)
    return HttpResponse(documento)

def cotizacion_real(request):
    real = Reais.objects.all()
    dicc = {'real': real}
    template = loader.get_template("real.html")
    documento = template.render(dicc)
    return HttpResponse(documento)


def index(request):
    template = loader.get_template("index.html")
    documento = template.render()
    return HttpResponse(documento)


