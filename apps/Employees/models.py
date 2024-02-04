from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

def user_directory_path(instance, filename):
    return "employees/{0}/{1}".format(instance.name, filename)

def skills_directory_path(instance, filename):
    return "skills/{0}/{1}".format(instance.skill, filename)

def certificate_directory_path(instance, filename):
    return "certificates/{0}/{1}".format(instance.name, filename)


class SkillCategory(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
 
class Skills(models.Model):
    skill = models.CharField(max_length=255)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to=skills_directory_path,max_length=1024)
    
    def __str__(self):
        return self.skill


class EmployeeCategory(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
    
    
class Employee(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField()
    image = models.ImageField(upload_to=user_directory_path, max_length=1024)
    position = models.ForeignKey(EmployeeCategory, on_delete=models.PROTECT)
    skills = models.ManyToManyField(Skills, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    
class EmploymentHistory(models.Model):
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    description = RichTextField()
    from_date = models.DateField()
    to_date = models.DateField(null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.company_name
    
    
class Certificates(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=certificate_directory_path, max_length=1024)
    url = models.URLField(max_length=1024)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.name
    

