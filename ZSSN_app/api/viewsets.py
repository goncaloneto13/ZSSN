from ZSSN_app import models
from rest_framework import viewsets
from ZSSN_app.api import serializer
from ZSSN_app import models

class SobreviventeViewSet(viewsets.ModelViewSet):
    serializer_class= serializer.SobreviventeSerializer
    queryset = models.Sobrevivente.objects.all()

class InventarioViewSet(viewsets.ModelViewSet):
    serializer_class= serializer.InventarioSerializer
    queryset = models.Inventario.objects.all()    