from django.contrib import admin

# Register your models here.

from .models import Profile, Status, FriendRequest

admin.site.register(Profile)
admin.site.register(Status)
admin.site.register(FriendRequest)