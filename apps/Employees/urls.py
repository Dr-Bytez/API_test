from django.urls import path
from . import views

urlpatterns = [
    path('employees', views.EmployeesView.as_view()),
    path('employee/<int:pk>', views.SingleEmployeeView.as_view()),
]