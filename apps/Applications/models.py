from django.db import models

# Create your models here.

class Application(models.Model):
    name = models.CharField(max_length=255)
    messenger = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        self.name