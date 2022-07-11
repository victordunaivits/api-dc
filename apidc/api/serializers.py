from rest_framework import serializers
from apidc import models

class HeroiSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Herois
        fields = '__all__'
