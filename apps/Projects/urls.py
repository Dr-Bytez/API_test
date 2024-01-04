from django.urls import path
from . import views

urlpatterns = [
    path('projects', views.ProjectView.as_view()),
    path('<int:pk>', views.SingleProjectView.as_view()),
]