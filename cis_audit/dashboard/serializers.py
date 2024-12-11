# serializers.py
from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'email', 'role', 'platform', 'last_login', 'audits_performed']

    # Custom method to map User's email and role
    email = serializers.EmailField(source="user.email", read_only=True)
    role = serializers.CharField(source="user.groups.first.name", read_only=True)
