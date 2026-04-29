from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    full_name = models.CharField(max_length=150, blank=True, null=True)

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('banned', 'Banned'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )

    last_seen = models.DateTimeField(null=True, blank=True)

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    bio = models.TextField(blank=True, null=True)

    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    privacy_level = models.CharField(
        max_length=20,
        choices=[
            ('public', 'Public'),
            ('private', 'Private'),
        ],
        default='public'
    )

    def __str__(self):
        return f"Profile of {self.user.username}"