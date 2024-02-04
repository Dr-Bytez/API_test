from django.contrib import admin
from .models import *
# Register your models here.


class EmploymentHistoryAdmin(admin.StackedInline):
    model = EmploymentHistory
    extra = 0
    
    
class CertificatesAdmin(admin.StackedInline):
    model = Certificates
    extra = 0
    
    
    
class EmployeeAdmin(admin.ModelAdmin):
    inlines = [EmploymentHistoryAdmin,CertificatesAdmin]
    

admin.site.register(EmployeeCategory)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(EmploymentHistory)
admin.site.register(Skills)
admin.site.register(Certificates)
admin.site.register(SkillCategory)