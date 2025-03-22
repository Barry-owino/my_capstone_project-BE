from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class Users(AbstractUser):
    date_of_membership = models.DateField(auto_now_add=True)
    is_active_member = models.BooleanField(default=True)

    def __str__(self):
        return self.username
