from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.email
