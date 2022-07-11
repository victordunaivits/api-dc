from rest_framework import viewsets
from apidc.api import serializers
from apidc import models

class HeroisViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.HeroiSerializer
    queryset = models.Herois.objects.all()
