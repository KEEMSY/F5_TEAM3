from django.contrib import admin

from .models import Blog, Profile, User

# Register your models here.
admin.site.register(User)
admin.site.register(Blog)
admin.site.register(Profile)

