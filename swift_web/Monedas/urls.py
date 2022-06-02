from nturl2path import url2pathname
from django.urls import path
from . import views

urlpatterns = [
    
    path("dolar/", views.cotizacion_dolar, name="dolar"),
    path("euro/", views.cotizacion_euro, name="euro"),
    path("dolar_blue/", views.cotizacion_dolar_blue, name="dolar_blue"),
    path("real/", views.cotizacion_real, name="real"),
]
