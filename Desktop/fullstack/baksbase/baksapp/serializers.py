from rest_framework import serializers
from .models import Fuel, oil

class FuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        fields = '__all__'

class OilSerializer(serializers.ModelSerializer):
    class Meta:
        model = oil
        fields = '__all__'