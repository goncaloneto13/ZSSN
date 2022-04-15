from dataclasses import fields
from pyexpat import model
from django import forms

from ZSSN_app.models import Inventario, Sobrevivente

class SobreviventeForm(forms.ModelForm):
    class Meta:
        model = Sobrevivente
        fields = '__all__'
        exclude = ['acusacoes','acusacao1','acusacao2','acusacao3','Infectado','Água','Alimento','Medicação','Munição']

class LocalForm(forms.ModelForm):
    class Meta:
        model=Sobrevivente
        fields = ['Log','Lat'] 

class AcusacoesForm(forms.ModelForm):
    class Meta:
        model = Sobrevivente
        fields = ['acusacoes']

class InventarioForm(forms.ModelForm):
    class Meta:
        model= Inventario
        fields = ['agua','alimento','medicacao','municao']
