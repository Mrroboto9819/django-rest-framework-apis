import email
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    web_site = models.CharField(max_length=400, blank=True)
    
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
