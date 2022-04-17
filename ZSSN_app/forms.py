from dataclasses import fields
from pyexpat import model
from django import forms

from ZSSN_app.models import Inventario, Sobrevivente

class SobreviventeForm(forms.ModelForm):

    class Meta:
        model = Sobrevivente
        exclude = ['infectado','acusacoes','infectados_relatados']
        widgets = { 'data_n': forms.DateInput(format=('%d-%m-%Y'), 
                                             attrs={'class':'data_n', 
                                            'placeholder':'dd/mm/aaaa'})
                    }

class LocalForm(forms.ModelForm):
    class Meta:
        model=Sobrevivente
        fields = ['log','lat'] 

class AcusacoesForm(forms.ModelForm):
    class Meta:
        model = Sobrevivente
        fields = ['acusacoes']

class InventarioForm(forms.ModelForm):
    class Meta:
        model= Inventario
        exclude = ['sobrevivente']
