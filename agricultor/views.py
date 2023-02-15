from django.shortcuts import render

#importar librerias
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
#importar modelo y formulario
from .models import Agricultor
from .forms import AgricultorForm


#Vista para listar agricultores
def listarAgricultor(request):
    Agricultor = Agricultor.objects.all()
    context = {'agricultor':Agricultor}
    template = loader.get_template('agricultor/agricultor.html')
    return HttpResponse(template.render(context,request))

#Vista para ver detalles de un agricultor
def agricultor_view(request, id):
    context = {}
    context['object'] = Agricultor.objects.get(id = id)
    return render(request,'agricultor/agricultor_detalle.html',context)

#vista para crear autores.
def crear_agricultor(request):
    context = {}
    form = AgricultorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('agricultor')    
    context['form'] = form
    return render(request,'agricultor/crear_agricultor.html', context)


#vista para actualizar agricultores
#Referencia https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/?ref=lbp
def update_agricultor(request,id):
    context = {}
    obj = get_object_or_404(Agricultor, id = id)
    #formulario que contiene la instancia
    form = AgricultorForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('agricultor')    
    context['form'] = form
    return render(request, "agricultor/actualizar_agricultor.html", context)


#Vista para eliminar un autor
def delete_view(request, id):
    context = {}
    obj = get_object_or_404(Agricultor, id = id)
    if request.method == "POST":
        obj.delete()
        return redirect('agricultor')    
    return render(request, "agricultor/eliminar_agricultor.html", context)