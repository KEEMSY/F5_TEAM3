from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=255, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Blog(models.Model):
    text = models.TextField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(blank=True)
    skill = models.CharField(max_length=100, blank=True)
    github = models.URLField(max_length=250, blank=True)
    blog = models.URLField(max_length=250, blank=True)









