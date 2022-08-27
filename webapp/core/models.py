from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Profile(models.Model):
    # login/basic user info
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_id = models.IntegerField()
    
    # profile info
    avatar = models.ImageField(upload_to=None, default='default.png')
    private = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # status info
    mood = models.IntegerField(default=0)

    # name objects by username
    def __str__(self):
        return self.user.username

