from email.policy import default
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
    Infectado = models.BooleanField(default=False,editable=False)
    acusacoes = models.PositiveIntegerField(editable=False,default=0)

    Água = models.PositiveIntegerField(default=0)
    Alimento = models.PositiveBigIntegerField(default=0)
    Medicação = models.PositiveBigIntegerField(default=0)
    Munição = models.PositiveBigIntegerField(default=0)
    

    Itens = [Água,Alimento,Medicação,Munição]

    ultimo_local = (Log,Lat)
    
    def __str__(self):
        return self.Nome

class Item(models.Model):

    nome = models.CharField(max_length=30)
    pontos =  models.PositiveIntegerField()

    def __str__(self):
        return self.nome


# Create your models here.
