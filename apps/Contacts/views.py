from rest_framework import generics
from rest_framework import filters
from .models import Contact
from .serializers import ContactSerializer

class ContacsView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [filters.SearchFilter,]
    search_fields = ['instagram', 'telegram', 'whatsapp','youtube', 'behance', 'email', 'phone',]