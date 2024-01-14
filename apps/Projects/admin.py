from django.contrib import admin
from .models import Project, ProjectImages
# Register your models here.


 
    
class ProjectImagesAdmin(admin.StackedInline):
    model = ProjectImages
    extra = 0
    
    
class ProjectsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}
    inlines = [ProjectImagesAdmin,]
    
        
admin.site.register(Project,ProjectsAdmin)