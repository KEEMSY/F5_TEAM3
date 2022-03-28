from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50, null=True, default='')
    email = models.EmailField(max_length=255, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Blog(models.Model):
    text = models.TextField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(blank=True)
    github = models.URLField(max_length=250, blank=True)
    blog = models.URLField(max_length=250, blank=True)

    SKILL_A = 'Python'
    SKILL_B = 'Django'
    SKILL_C = 'Java'
    SKILL_D = 'Flask'
    SKILL_E = None
    SKILL_CHOICES = [
        (SKILL_A, 'Python'),
        (SKILL_B, 'Django'),
        (SKILL_C, 'Java'),
        (SKILL_D, 'Flask'),
        (SKILL_E, '없음'),
    ]

    skill = models.CharField(max_length=100, blank=True, choices=SKILL_CHOICES)










