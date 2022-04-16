from dataclasses import fields
from pyexpat import model
from django import forms

from ZSSN_app.models import Inventario, Sobrevivente

class SobreviventeForm(forms.ModelForm):
    class Meta:
        model = Sobrevivente
        fields = '__all__'
        exclude = ['infectado','acusacoes','inventario']

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
        fields = ['agua','alimentacao','medicacao','municao']
