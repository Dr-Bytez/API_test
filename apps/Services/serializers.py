from rest_framework import serializers
from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    
    class Meta:
        model = Service
        fields = ['id', 'title', 'price', 'image', 'description', 'slug']