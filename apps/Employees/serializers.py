from rest_framework import serializers
from .models import *


class EmployeeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeCategory
        fields = ['id', 'title']
        

class EmployeeSerializer(serializers.ModelSerializer):
    position = EmployeeCategorySerializer()
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = Employee
        fields = ['id', 'name', 'description', 'image', 'position']