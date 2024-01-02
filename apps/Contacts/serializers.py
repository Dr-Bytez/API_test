from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['instagram', 'telegram', 'whatsapp','youtube', 'behance', 'email', 'phone']