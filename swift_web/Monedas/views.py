from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Dolar, Dolar_blue, Euro, Reais
import datetime

# Create your views here.

def index(request):
    template = loader.get_template("index.html")
    documento = template.render()
    return HttpResponse(documento)

def conversor(request):
    template = loader.get_template("conversor.html")
    documento = template.render()
    return HttpResponse(documento)

def contacto(request):
    template = loader.get_template("contacto.html")
    documento = template.render()
    return HttpResponse(documento)
