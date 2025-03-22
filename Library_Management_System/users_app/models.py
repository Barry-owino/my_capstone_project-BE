from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
# Create your models here.

class Users(AbstractUser):
    date_of_membership = models.DateField(auto_now_add=True)
    is_active_member = models.BooleanField(default=True)

     # Add groups and user_permissions with a unique related_name
    groups = models.ManyToManyField(
        Group,
        related_name='custom_users',  # unique name to avoid conflict
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # unique name to avoid conflict
        blank=True
    )

    def __str__(self):
        return self.username
