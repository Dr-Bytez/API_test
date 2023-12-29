from rest_framework import serializers
from .models import *


class EmployeeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeCategory
        fields = ['id', 'title']
        

class EmployeeSerializer(serializers.ModelSerializer):
    category = EmployeeCategorySerializer
    
    class Meta:
        model = Employee
        fields = ['id', 'name', 'category']