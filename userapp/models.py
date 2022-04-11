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
    img = models.FileField(upload_to='uploads/%Y%m%d', blank=True, null=True)
    github = models.URLField(max_length=250, blank=True)
    blog = models.URLField(max_length=250, blank=True)

    SKILL_A = 'Android'
    SKILL_B = 'iOS'
    SKILL_C = 'C++'
    SKILL_D = 'C#'
    SKILL_E = 'Java'
    SKILL_F = 'PHP'
    SKILL_G = 'Python'
    SKILL_H = 'Ruby'
    SKILL_I = 'JSP'
    SKILL_J = 'Node.js'
    SKILL_K = 'AngularJS'
    SKILL_L = 'jQuery'
    SKILL_M = 'ASP.NET'
    SKILL_N = None
    SKILL_CHOICES = [
        (SKILL_A, 'Android'),
        (SKILL_B, 'iOS'),
        (SKILL_C, 'C++'),
        (SKILL_D, 'C#'),
        (SKILL_E, 'Java'),
        (SKILL_F, 'PHP'),
        (SKILL_G, 'Python'),
        (SKILL_H, 'Ruby'),
        (SKILL_I, 'JSP'),
        (SKILL_J, 'Node.js'),
        (SKILL_K, 'AngularJS'),
        (SKILL_L, 'jQuery'),
        (SKILL_M, 'ASP.NET'),
        (SKILL_N, '없음'),
    ]

    skill = models.CharField(max_length=100, blank=True, choices=SKILL_CHOICES)










