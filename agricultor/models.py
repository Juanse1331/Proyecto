from django.db import models

# Create your models here.
class Agricultor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    #departamento = models.CharField(max_length=40)
    vereda = models.CharField(max_length=50)