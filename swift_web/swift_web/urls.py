"""swift_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from msilib.schema import ListView
from django.contrib import admin
from django.urls import path
from Monedas import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,),
    path('conversor/', views.conversor, name="conversor"),
    path('contacto/', views.contacto, name="contacto"),
    path('cotizaciones/', views.cotizaciones, name="cotizaciones"),
    path('landing_cotizacion/', views.landing_cotizacion, name="landing_cotizacion"),
    path('cotizacion_usd/', views.cotizacion_usd, name="cotizacion_usd"),
    path('cotizacion_usd_blue/', views.cotizacion_usd_blue, name="cotizacion_usd_blue"),
    path('cotizacion_euro/', views.cotizacion_euro, name="cotizacion_euro"),
    path('cotizacion_real/', views.cotizacion_real, name="cotizacion_real"),
    path('landing_busqueda/', views.SearchView.as_view(), name="busqueda"),
    ]
