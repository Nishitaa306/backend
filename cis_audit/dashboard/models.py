# models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=100)
    platform = models.CharField(max_length=255, default="Windows 11 & Linux")
    last_login = models.DateTimeField(auto_now=True)
    audits_performed = models.IntegerField(default=0)

    def __str__(self):
        return self.full_name
