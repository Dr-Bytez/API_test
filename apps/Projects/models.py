from django.db import models
from apps.Employees.models import Employee
# Create your models here.

def user_directory_path(instance, filename):
    return "projects/{0}/{1}".format(instance.title, filename)


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=user_directory_path,null=True, blank=True)
    slug = models.SlugField()
    url = models.CharField(max_length=255,null=True, blank=True)
    developers = models.ManyToManyField(Employee, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    