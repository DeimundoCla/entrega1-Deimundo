from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from sympy import Q
from . import models
from .forms import Usd_Form, Usd_blue_Form, Euro_Form, Real_Form, busqueda_Form
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

def cotizaciones(request):
    template = loader.get_template("cotizaciones.html")
    documento = template.render()
    return HttpResponse(documento)

def contacto(request):
    template = loader.get_template("contacto.html")
    documento = template.render()
    return HttpResponse(documento)

def landing_cotizacion(request):
    template = loader.get_template("landing_cotizacion.html")
    documento = template.render()
    return HttpResponse(documento)

def landing_busqueda(request):
    usd = None
    usd_blue = None
    euro = None
    real = None

    if 'q' in request.GET:
        q = request.GET['q']
        usd = models.Dolar.objects.filter(fecha__icontains=q)
        usd_blue = models.Dolar_blue.objects.filter(fecha__icontains=q)
        euro = models.Euro.objects.filter(fecha__icontains=q)
        real = models.Reais.objects.filter(fecha__icontains=q)
    else:
        q = (models.Dolar.objects.all, models.Dolar_blue.objects.all, models.Euro.objects.all, models.Reais.objects.all)
    
    
    return render (request, 'landing_busqueda.html', {'usd': usd, 'usd_blue': usd_blue, 'euro': euro, 'real': real})

def cotizacion_usd(request):
    if request.method == "POST":
        form_usd = Usd_Form(request.POST)
        if form_usd.is_valid():
            form_usd.save()
            return HttpResponseRedirect("/landing_cotizacion/")
        else:
            return render(request, "cotizacion_usd.html",  {'form': form_usd})
    form = Usd_Form
    return render(request, "cotizacion_usd.html",  {'form': form})

def cotizacion_usd_blue(request):
    if request.method == "POST":
        form_usd_blue = Usd_blue_Form(request.POST)
        if form_usd_blue.is_valid():
            form_usd_blue.save()
            return HttpResponseRedirect("/landing_cotizacion/")
    
    form = Usd_blue_Form
    return render(request, "cotizacion_usd_blue.html",  {'form': form})

def cotizacion_euro(request):
    if request.method == "POST":
        form_euro = Euro_Form(request.POST)
        if form_euro.is_valid():
            form_euro.save()
            return HttpResponseRedirect("/landing_cotizacion/")
    
    form = Euro_Form
    return render(request, "cotizacion_euro.html",  {'form': form})

def cotizacion_real(request):
    if request.method == "POST":
        form_real = Real_Form(request.POST)
        if form_real.is_valid():
            form_real.save()
            return HttpResponseRedirect("/landing_cotizacion/")
    
    form = Real_Form
    return render(request, "cotizacion_real.html",  {'form': form})