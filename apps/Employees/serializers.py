from rest_framework import serializers
from .models import *


class EmployeeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeCategory
        fields = ['id', 'title',]
        
      
class EmploymentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentHistory
        fields = ['id', 'title', 'company_name', 'description', 'from_date', 'to_date',]
    
    
class SkillCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SkillCategory
        fields = ['id','name',]
   
        
class SkillsSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    category = SkillCategorySerializer(read_only=True)
    class Meta:
        model = Skills
        fields = ['id', 'skill', 'category','image',]
   
        
class CertificatesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = Certificates
        fields = ['id', 'name', 'image', 'url',]
        

class EmployeeSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    position = EmployeeCategorySerializer()
    employment_history = EmploymentHistorySerializer(many=True)
    skills = SkillsSerializer(many=True)
    certificates = CertificatesSerializer(many=True)
    class Meta:
        model = Employee
        fields = ['id', 'name', 'description', 'image', 'position', 'employment_history', 'skills', 'certificates',]