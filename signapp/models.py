from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    occupation = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username
