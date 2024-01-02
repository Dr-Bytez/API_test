from django.contrib import admin
from .models import Service
# Register your models here.



class ServicesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}
        
admin.site.register(Service,ServicesAdmin)