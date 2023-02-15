from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('agricultor/', views.listarAgricultor, name='agricultor'),
    path('agricultor/new', views.crear_agricultor, name='nuevo_agricultor'),
    path('agricultor/<id>/', views.agricultor_view, name='agricultor_view'),
    path('agricultor/update/<id>/', views.update_agricultor, name='agricultor_actualizar'),
    path('agricultor/delete/<id>/', views.delete_view, name='agricultor_eliminar'),
]