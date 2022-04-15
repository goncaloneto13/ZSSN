from dataclasses import fields
from pyexpat import model
from django import forms

from ZSSN_app.models import Sobrevivente

class SobreviventeForm(forms.ModelForm):
    class Meta:
        model = Sobrevivente
        fields = '__all__'
        exclude = ['acusacoes','acusacao1','acusacao2','acusacao3','Infectado']

class LocalForm(forms.ModelForm):
    class Meta:
        model=Sobrevivente
        fields = ['Log','Lat'] 

class ItensForm(forms.ModelForm):
    class Meta:
        model=Sobrevivente
        fields = ['Água','Alimento','Medicação','Munição']

class AcusacoesForm(forms.ModelForm):
    class Meta:
        model = Sobrevivente
        fields = ['acusacoes']