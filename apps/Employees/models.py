from django.db import models

# Create your models here.

def user_directory_path(instance, filename):
    return "employees/{0}/{1}".format(instance.name, filename)



class EmployeeCategory(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
    
class Employee(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to=user_directory_path, max_length=255)
    position = models.ForeignKey(EmployeeCategory, on_delete=models.PROTECT)
    
    
    def __str__(self):
        return self.name