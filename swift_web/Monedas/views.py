from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from sympy import Q
from Monedas.models import *
from .forms import *
from itertools import chain
from django.views.generic import ListView


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


class SearchView(ListView):
    template_name = 'landing_busqueda.html'
    paginate_by = 20
    count = 0
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)
       
        if query is not None:
            resultados_dolar        = Dolar.objects.filter(query)
            resultados_euro      = Euro.objects.filter(query)
            resultados_dolar_blue     = Dolar_blue.objects.filter(query)
            resultados_real                = Reais.objects.filter(query)
            
            # combinar las búsquedas 
            queryset_chain = chain(
                    resultados_dolar,
                    resultados_euro,
                    resultados_dolar_blue,
                    resultados_real,
            )        
            qs = sorted(queryset_chain, 
                        key=lambda instance: instance.pk, 
                        reverse=True)
            self.count = len(qs) # el resultado es una lista
            return qs
        return Dolar.objects.none() # por Default debería ir una lista vacía