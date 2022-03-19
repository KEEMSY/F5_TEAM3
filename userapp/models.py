from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=255, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Skill(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.CharField(max_length=100, blank=True)

class Contact(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    github = models.CharField(max_length=100, blank=True)
    linkedin = models.CharField(max_length=100, blank=True)
    blog = models.CharField(max_length=100, blank=True)

class Blog(models.Model):
    text = models.TextField()



