from django.db import models
from ckeditor.fields import RichTextField
from apps.Employees.models import Employee
# Create your models here.

def user_directory_path(instance, filename):
    return "projects/{0}/{1}".format(instance.title, filename)

def image_directory_path(instance, filename):
    return "projects/{0}/{1}".format(instance.project.title, filename)





class Project(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(max_length=1024,upload_to=user_directory_path,null=True, blank=True)
    slug = models.SlugField()
    url = models.CharField(max_length=1024,null=True, blank=True)
    developers = models.ManyToManyField(Employee, null=True, blank=True)
    
    
    def __str__(self):
        return self.title
    
    
class ProjectImages(models.Model):
    image = models.ImageField(upload_to=image_directory_path)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_images')