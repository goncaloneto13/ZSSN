from email.policy import default
from xml.etree.ElementInclude import default_loader
from django.db import models
#from uuid import uuid4


class Sobrevivente(models.Model):

    SEXO_CHOICES =(
        ("F","Feminino"),
        ("M","Masculino")
    )

    nome = models.CharField(max_length=255)
    idade = models.PositiveIntegerField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=False, blank=False)
    log = models.DecimalField('Longitude', max_digits=9, decimal_places=6)
    lat = models.DecimalField('Latitude',max_digits=9, decimal_places=6)
    infectado = models.BooleanField(default=False)
    acusacoes = models.PositiveIntegerField('acusações',default=0)
    acusado_id = []
    itens = ['Água','Alimento','Medicação','Munição']

    ultimo_local = (log,lat)
    
    def __str__(self):
        return self.nome

            


class Inventario(models.Model):

    sobrevivente = models.ForeignKey(Sobrevivente,on_delete= models.CASCADE)
    agua = models.PositiveIntegerField('Água',default=0)
    alimento = models.PositiveBigIntegerField('Alimento',default=0)
    medicacao = models.PositiveBigIntegerField('Medicação',default=0)
    municao = models.PositiveBigIntegerField('Munição',default=0)

    def total_pontos(self):
        return self.agua + self.alimento + self.medicacao + self.municao


# Create your models here.
