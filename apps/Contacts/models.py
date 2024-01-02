from django.db import models

# Create your models here.

class Contact(models.Model):
    instagram = models.CharField(max_length=255, null=True, blanl=True)
    telegram = models.CharField(max_length=255, null=True, blanl=True)
    whatsapp = models.CharField(max_length=255, null=True, blanl=True)
    youtube = models.CharField(max_length=255, null=True, blanl=True)
    behance = models.CharField(max_length=255, null=True, blanl=True)
    email = models.EmailField(max_length=255, null=True, blanl=True)
    phone = models.CharField(max_length=255, null=True, blanl=True)