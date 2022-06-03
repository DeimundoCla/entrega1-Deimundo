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

def cotizaciones(request):
    template = loader.get_template("cotizaciones.html")
    documento = template.render()
    return HttpResponse(documento)

def landing_cotizacion(request):
    template = loader.get_template("landing_cotizacion.html")
    documento = template.render()
    return HttpResponse(documento)

def alta_usd(request):
        if request.method == "POST":
            usd_cotizacion = Dolar( cotizacion = request.POST["cotizacion-usd"], fecha = request.POST["fecha-cotizacion"], variacion = request.POST["variacion-cotizacion"])
            usd_cotizacion.save()
        return render (request, 'cotizaciones.html')
        

def alta_usd_blue(request):
    if request.method == "POST":
        usd_blue_cotizacion = Dolar_blue( cotizacion = request.POST["cotizacion-usd-blue"], fecha = request.POST["fecha-cotizacion-blue"], variacion = request.POST["variacion-cotizacion-blue"])
        usd_blue_cotizacion.save()
        return render (request, 'landing_cotizacion.html')
    else:
        return render (request, 'cotizaciones.html')

def alta_euro(request):
    if request.method == "POST":
        euro_cotizacion = Euro( cotizacion = request.POST["cotizacion-euro"], fecha = request.POST["fecha-cotizacion_euro"], variacion = request.POST["variacion-cotizacion_euro"])
        euro_cotizacion.save()
        return render (request, 'landing_cotizacion.html')
    else:
        return render (request, 'cotizaciones.html')

def alta_real(request):
    if request.method == "POST":
        real_cotizacion = Reais( cotizacion = request.POST["cotizacion-real"], fecha = request.POST["fecha-cotizacion_real"], variacion = request.POST["variacion-cotizacion_real"])
        real_cotizacion.save()
        return render (request, 'landing_cotizacion.html')
    else:
        return render (request, 'cotizaciones.html')