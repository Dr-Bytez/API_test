from django.db import models

# Create your models here.

def user_directory_path(instance, filename):
    return "employees/{0}/{1}".format(instance.name, filename)

def skills_directory_path(instance, filename):
    return "skills/{0}/{1}".format(instance.skill, filename)

def certificate_directory_path(instance, filename):
    return "certificates/{0}/{1}".format(instance.certificate_name, filename)


class EmployeeCategory(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
    
class EmploymentHistory(models.Model):
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    description = models.TextField()
    from_date = models.DateField()
    to_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.company_name
    
    
class Skills(models.Model):
    skill = models.CharField(max_length=255)
    image = models.ImageField(upload_to=skills_directory_path)
    
    def __str__(self):
        return self.skill
    
class Certificates(models.Model):
    certificate_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=certificate_directory_path)
    url = models.URLField()
    
    def __str__(self):
        return self.certificate_name
    
class Employee(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to=user_directory_path, max_length=255)
    position = models.ForeignKey(EmployeeCategory, on_delete=models.PROTECT)
    employment_history = models.ManyToManyField(EmploymentHistory, null=True, blank=True)
    skills = models.ManyToManyField(Skills, null=True, blank=True)
    certificates = models.ManyToManyField(Certificates, null=True, blank=True)
    
    def __str__(self):
        return self.name