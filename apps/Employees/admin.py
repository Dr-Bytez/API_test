from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(EmployeeCategory)
admin.site.register(Employee)
admin.site.register(EmploymentHistory)
admin.site.register(Skills)
admin.site.register(Certificates)
admin.site.register(SkillCategory)