from django.contrib import admin

# Register your models here.

from .models import Profile, Status

admin.site.register(Profile)
admin.site.register(Status)