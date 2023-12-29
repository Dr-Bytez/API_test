from django.urls import path, include

urlpatterns = [
    path('employees/', include('apps.Employees.urls')),
]