from django.db import models
from datetime import date


class Euro(models.Model):
    nombre = models.CharField(max_length=50, default="Euro")
    simbolo = "€"
    cotizacion = models.FloatField()
    fecha = models.DateField(default=date.today)
    variacion = models.DecimalField(max_digits=3, decimal_places=0)


class Dolar(models.Model):
    nombre = models.CharField(max_length=50, default="Dolar")
    simbolo = "U$S"
    cotizacion = models.FloatField()
    fecha = models.DateField(default=date.today)
    variacion = models.DecimalField(max_digits=3, decimal_places=0)
    

class Dolar_blue(models.Model):
    nombre = models.CharField(max_length=50, default="Dolar Blue")
    simbolo = "USD"
    cotizacion = models.FloatField()
    fecha = models.DateField(default=date.today)
    variacion = models.DecimalField(max_digits=3, decimal_places=0)


class Reais(models.Model):
    nombre = models.CharField(max_length=50, default="Real")
    simbolo = "R$"
    cotizacion = models.FloatField()
    fecha = models.DateField(default=date.today)
    variacion = models.DecimalField(max_digits=3, decimal_places=0)
    

