from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Application
from .serializers import ApplicationSerializer

class ApplicationView(generics.CreateAPIView):
    queryset = Application
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated,]
    