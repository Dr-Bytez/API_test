from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContacsView.as_view()),
]