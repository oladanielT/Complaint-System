from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('staff', 'staff'),
        ('engineer', 'engineer'),
        ('admin', 'admin')
    )

    role = models.CharField(max_length=25, choices=ROLE_CHOICES, default='staff')

    def __str__(self):
        return f"{self.username} ({self.role})"