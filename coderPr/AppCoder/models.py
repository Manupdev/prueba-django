from django.db import models

class Familia(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    fecha = models.DateField()
    
