from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    age = models.IntegerField(default=18)
    bio = models.TextField(max_length=400, null=True, blank=True)
