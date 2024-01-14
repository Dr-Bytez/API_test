from rest_framework import serializers
from .models import *


class EmployeeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeCategory
        fields = ['id', 'title',]
        
      
class EmploymentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentHistory
        fields = ['id', 'job_title', 'company_name', 'description', 'from_date', 'to_date',]
    
        
class SkillsSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = Skills
        fields = ['id', 'skill', 'image',]
   
        
class CertificatesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = Certificates
        fields = ['id', 'certificate_name', 'image', 'url',]
        

class EmployeeSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    position = EmployeeCategorySerializer()
    employment_history = EmploymentHistorySerializer(many=True)
    skills = SkillsSerializer(many=True)
    certificates = CertificatesSerializer(many=True)
    class Meta:
        model = Employee
        fields = ['id', 'name', 'description', 'image', 'position', 'employment_history', 'skills', 'certificates',]