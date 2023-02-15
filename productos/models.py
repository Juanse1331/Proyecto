from django.db import models

from agricultor.models import Agricultor

# Create your models here.
class producto (models.Model):
    agricultor = models.ForeignKey(Agricultor, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    imagen=models.ImageField()
    precio=models.CharField(max_length=200)
    description=models.CharField(max_length=500)


    
