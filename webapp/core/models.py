from django.db import models
class Users(models.Model):
    username = models.CharField(max_length=24)
    user_id = models.IntegerField()
    password = models.CharField(max_length=24)
    email = models.EmailField(max_length=320)
    #profilepicture = models.ImageField(upload_to='profilepictures/')
    private = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

