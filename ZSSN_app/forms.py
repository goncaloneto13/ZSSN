from pyexpat import model
from django import forms

from ZSSN_app.models import Sobrevivente

class SobreviventeForm(forms.ModelForm):
    class Meta:
        model = Sobrevivente
        fields = '__all__'

class LocalForm(forms.ModelForm):
    class Meta:
        model=Sobrevivente
        fields = ['Log','Lat'] 