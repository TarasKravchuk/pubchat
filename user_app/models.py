from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ChatUser (models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_email = models.EmailField(max_length=120, default=None)
    registration_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
