from django import forms
from .models import Agricultor

#Crear formulario
class AgricultorForm(forms.ModelForm):

    #metaclase
    class Meta:
        model = Agricultor

        #especificar los campos
        fields = [
            'nombre',
            'apellido',
            #'depertamento',
            'vereda'
        ]