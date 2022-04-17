from email.policy import default
from operator import truediv
from xml.etree.ElementInclude import default_loader
from django.db import models
from django.contrib.postgres.fields import ArrayField
from datetime import datetime

#from uuid import uuid4



class Inventario(models.Model):

    agua = models.PositiveIntegerField('Água',default=0)
    alimentacao = models.PositiveBigIntegerField('Alimentação',default=0)
    medicacao = models.PositiveBigIntegerField('Medicação',default=0)
    municao = models.PositiveBigIntegerField('Munição',default=0)

    def total_pontos(self):
        return self.agua + self.alimentacao + self.medicacao + self.municao

    def quant_itens(self):
        return [self.agua,self.alimentacao,self.medicacao,self.municao]    
    
    def pontos_itens(self):
        return {'Água': 4,'Alimentação': 3,'Medicação': 2 ,'Munição': 1}


class Sobrevivente(models.Model):


    SEXO_CHOICES =(
        ("F","Feminino"),
        ("M","Masculino")
    )

    nome = models.CharField(max_length=255)
    data_n = models.DateField('Data de Nascimento')
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=False, blank=False)
    log = models.DecimalField('Longitude', max_digits=9, decimal_places=6)
    lat = models.DecimalField('Latitude',max_digits=9, decimal_places=6)
    infectado = models.BooleanField(default=False)
    acusacoes = models.PositiveIntegerField('acusações',default=0)
    infectados_relatados = ArrayField(models.IntegerField(blank=True),default= list, blank=True)
    
    itens = ['Água','Alimentação','Medicação','Munição']
    inventario = models.ForeignKey(Inventario,on_delete=models.CASCADE,default=False)

    ultimo_local = (log,lat)
    
    def __str__(self):
        return self.nome

    def Sexo(self):
        if self.sexo == self.SEXO_CHOICES[0][0]:
            return self.SEXO_CHOICES[0][1]
        return self.SEXO_CHOICES[1][1]


    def idade(self):
        born = self.data_n
        today = datetime.today()
        return today.year - born.year - ((today.month,  today.day) < (born.month, born.day))
    

# Create your models here.
