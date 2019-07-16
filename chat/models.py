from django.db import models
from user_app.models import ChatUser

# Create your models here.

class user_message (models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', unique=True)
    author = models.ForeignKey(ChatUser, on_delete=models.PROTECT)
    time = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=120, default=None)
    message = models.TextField(max_length=99, default=None)

    def __str__(self):
        return '№ ' + str(self.id) + ' от ' + str(self.author)

    class Meta:
        ordering = ['time']


class message (models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', unique=True)
    time = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=120, default=None)
    message = models.TextField(max_length=99, default=None)

    def __str__(self):
        return  '№ ' + str(self.id) + ' от ' + self.email

    class Meta:
        ordering = ['time']
