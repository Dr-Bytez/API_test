from django.urls import path, include

urlpatterns = [
    path('employees/', include('apps.Employees.urls')),
    path('applications/', include('apps.Applications.urls')),
    path('services/', include('apps.Services.urls')),
    path('contacts/', include('apps.Contacts.urls')),
    path('projects/', include('apps.Projects.urls')),
]