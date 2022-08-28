from django.contrib import admin

# Register your models here.

from .models import Profile, Status, FriendRequest, Hug

admin.site.register(Profile)
admin.site.register(Status)
admin.site.register(FriendRequest)
admin.site.register(Hug)