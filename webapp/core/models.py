import profile
from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()
class Profile(models.Model):
    # login/basic user info
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_id = models.IntegerField()
    
    # profile info
    avatar = models.ImageField(upload_to='profile_pictures', default='default.jpg')
    private = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # status info
    mood = models.IntegerField(default=0)

    # name objects by username
    def __str__(self):
        return self.user.username

class Status(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    mood = models.IntegerField(default=0)
    message = models.TextField(max_length=500)
    def __str__(self):
        return self.user