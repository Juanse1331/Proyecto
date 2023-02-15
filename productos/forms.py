from django import forms
from .models import Productos

#Crear formulario
class ProductosForm(forms.ModelForm):

    #metaclase
    class Meta:
        model = Productos

        #especificar los campos
        fields = [
            'tittle',
            'precio',
            'descripcion',
            
        ]