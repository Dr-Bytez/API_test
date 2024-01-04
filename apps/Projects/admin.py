from django.contrib import admin
from .models import Project
# Register your models here.

class ProjectsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}
        
admin.site.register(Project,ProjectsAdmin)