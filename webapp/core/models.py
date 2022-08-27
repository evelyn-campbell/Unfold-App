from django.db import models
class Users(models.Model):
    username = models.CharField(max_length=24)
    password = models.CharField(max_length=24)
    email = models.EmailField(max_length=320)
    private = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)



