from django.db import models

# Create your models here.

def user_directory_path(instance, filename):
    return "services/{0}/{1}".format(instance.title, filename)


class Service(models.Model):
    title = models.CharField(max_length=255)
    price = models.SmallIntegerField()
    image = models.ImageField(upload_to=user_directory_path)
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    
    def __str__(self):
        return self.title
