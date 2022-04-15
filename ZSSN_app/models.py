from email.policy import default
from xml.etree.ElementInclude import default_loader
from django.db import models
#from uuid import uuid4


class Sobrevivente(models.Model):

    SEXO_CHOICES =(
        ("F","Feminino"),
        ("M","Masculino")
    )

    #id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    Nome = models.CharField(max_length=255)
    Idade = models.PositiveIntegerField()
    Sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=False, blank=False)
    Log = models.DecimalField(max_digits=9, decimal_places=6)
    Lat = models.DecimalField(max_digits=9, decimal_places=6)
    Infectado = models.BooleanField(default=False)
    acusacoes = models.PositiveIntegerField(default=0)
 
    Itens = ['Água','Alimento','Medicação','Munição']

    ultimo_local = (Log,Lat)
    
    def __str__(self):
        return self.Nome


class Inventario(models.Model):

    sobrevivente = models.ForeignKey(Sobrevivente,on_delete= models.CASCADE)
    agua = models.PositiveIntegerField(default=0)
    alimento = models.PositiveBigIntegerField(default=0)
    medicacao = models.PositiveBigIntegerField(default=0)
    municao = models.PositiveBigIntegerField(default=0)


# Create your models here.
