# users/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Add any additional fields if needed
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    # Override related_name for groups and user_permissions to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='user_groups',  # Custom related_name to avoid clash
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='user_permissions',  # Custom related_name to avoid clash
        blank=True
    )

    def __str__(self):
        return self.username
