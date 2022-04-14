from dataclasses import fields
from rest_framework import serializers
from ZSSN_app import models

class ZSSNSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sobrevivente
        fields = '__all__'