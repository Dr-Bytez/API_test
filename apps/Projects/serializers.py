from rest_framework import serializers
from apps.Employees.serializers import EmployeeSerializer
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    developers = EmployeeSerializer(many=True)
    
    
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'image', 'slug', 'url', 'developers']