from ZSSN_app import models
from rest_framework import viewsets
from ZSSN_app.api import serializer
from ZSSN_app import models

class ZSSNViewSet(viewsets.ModelViewSet):
    serializer_class= serializer.ZSSNSerializer
    queryset = models.Sobrevivente.objects.all()