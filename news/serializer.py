from rest_framework import serializers
from .models import Moringamerch

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moringamerch
        fields = ('name', 'description', 'price')