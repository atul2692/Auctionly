from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.user.username

class Contact(models.Model):
    name = models.CharField(max_length=200)
    mail = models.EmailField()
    mobile = models.BigIntegerField(unique=True)
    text = models.CharField(max_length=500)
    def __str__(self):
        return self.name
    