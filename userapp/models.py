from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):

    email = models.EmailField(max_length=255, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

class Skill(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.CharField(max_length=100, blank=True)

class Contact(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    github = models.CharField(max_length=100, blank=True)
    linkedin = models.CharField(max_length=100, blank=True)
    blog = models.CharField(max_length=100, blank=True)



