from django.db import models
from datetime import date

# Create your models here.


class Euro(models.Model):
    nombre = "Euro"
    simbolo = "€"
    cotizacion = models.FloatField()
    fecha = models.DateField(default=date.today)
    variacion = models.DecimalField(max_digits=3, decimal_places=0)

class Dolar(models.Model):
    nombre = "Dólar Oficial"
    simbolo = "U$S"
    cotizacion = models.FloatField()
    fecha = models.DateField(default=date.today)
    variacion = models.DecimalField(max_digits=3, decimal_places=0)

class Dolar_blue(models.Model):
    nombre = "Dólar Blue"
    simbolo = "USD"
    cotizacion = models.FloatField()
    fecha = models.DateField(default=date.today)
    variacion = models.DecimalField(max_digits=3, decimal_places=0)


class Reais(models.Model):
    nombre = "Real"
    simbolo = "R$"
    cotizacion = models.FloatField()
    fecha = models.DateField(default=date.today)
    variacion = models.DecimalField(max_digits=3, decimal_places=0)
