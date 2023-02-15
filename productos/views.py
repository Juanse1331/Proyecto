#from django.shortcuts import render
#from .models import producto
from django.template import loader
from django.http import HttpResponse
#HttpResponseRedirect
#from django.shortcuts import get_object_or_404, redirect, render
# Create your views here.

def index(request):
    template = loader.get_template("index.html")
    #productos=producto.objects.all()
    #"productos":productos
    context={}
    #template =loader.get_template()
    return HttpResponse(template.render(context, request))