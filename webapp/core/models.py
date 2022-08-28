from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()
class Profile(models.Model):
    # login/basic user info
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_id = models.IntegerField()
    
    # profile info
    avatar = models.ImageField(upload_to='profile_pictures', default='default.png')
    private = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # status info
    mood = models.IntegerField(default=0)

    # friends
    friends = models.ManyToManyField("Profile", blank=True)

    # name objects by username
    def __str__(self):
        return self.user.username

class FriendRequest(models.Model):
    from_user = models.ForeignKey(Profile, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(Profile, related_name='to_user', on_delete=models.CASCADE)

class Status(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    mood = models.IntegerField(default=0)
    mood_icon = models.ImageField(upload_to='mood_pictures', default='happy.png')
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.user

    def get_mood_icon(self, mood):
        mood_to_icon = {'0': 'happy.png', '1': 'neutral.png', '2': 'sad.png', '3': 'anxious.png', '4': 'angry.png'}
        mood_icon = models.ImageField(upload_to='mood_pictures', default=mood_to_icon[str(mood)])
        return mood_icon