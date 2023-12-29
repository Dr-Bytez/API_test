from django.db import models

# Create your models here.

class EmployeeCategory(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
    
class Employee(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(EmployeeCategory, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name