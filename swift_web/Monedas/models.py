from django.db import models
from datetime import date
from django.db.models import Q

class SetQuery(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(nombre__icontains=query) | 
                         Q(fecha=query)|
                         Q(cotizacion__icontains=query)
                        )
            
            qs = qs.filter(or_lookup).distinct() 
            # distinct() por lo que leí muchas veces es requisito para las búsquedas múltiples con Q.

        return qs

class ManagerQuery(models.Manager):
    def get_queryset(self):
        return SetQuery (self.model, using=self._db)
    def search(self, query=None):
        return self.get_queryset().search(query=query)

class Euro(models.Model):
    nombre = models.CharField(max_length=50, default="Euro")
    simbolo = "€"
    cotizacion = models.FloatField()
    fecha = models.DateField(default=date.today)
    variacion = models.DecimalField(max_digits=3, decimal_places=0)

    objects = ManagerQuery()

class Dolar(models.Model):
    nombre = models.CharField(max_length=50, default="Dolar")
    simbolo = "U$S"
    cotizacion = models.FloatField()
    fecha = models.DateField(default=date.today)
    variacion = models.DecimalField(max_digits=3, decimal_places=0)
    
    objects = ManagerQuery()

class Dolar_blue(models.Model):
    nombre = models.CharField(max_length=50, default="Dolar Blue")
    simbolo = "USD"
    cotizacion = models.FloatField()
    fecha = models.DateField(default=date.today)
    variacion = models.DecimalField(max_digits=3, decimal_places=0)

    objects = ManagerQuery()


class Reais(models.Model):
    nombre = models.CharField(max_length=50, default="Real")
    simbolo = "R$"
    cotizacion = models.FloatField()
    fecha = models.DateField(default=date.today)
    variacion = models.DecimalField(max_digits=3, decimal_places=0)
    
    objects = ManagerQuery()
