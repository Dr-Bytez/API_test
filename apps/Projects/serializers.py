from rest_framework import serializers
from apps.Employees.serializers import EmployeeSerializer
from .models import Project, ProjectImages


class ProjectImagesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = ProjectImages
        fields = ['id', 'image',]
        

class ProjectSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    developers = EmployeeSerializer(many=True)
    
    project_images = ProjectImagesSerializer(many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'image', 'slug', 'url', 'developers', 'project_images',]
        

    
    
    
