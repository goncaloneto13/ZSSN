from dataclasses import fields
from rest_framework import serializers
from ZSSN_app import models

class SobreviventeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sobrevivente
        fields = '__all__'

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Inventario
        fields = '__all__'        