from rest_framework import serializers
from .models import user_message, message
from user_app.serializator import UserSerialization


class MessageSerialization (serializers.ModelSerializer):
    class Meta:
        model = message
        fields = ['id', 'time', 'email', 'message']


class UserMessageSerialization (serializers.ModelSerializer):
    author = UserSerialization()
    class Meta:
        model = user_message
        fields = ['id', 'author', 'time', 'email', 'message']


class MessagePostSerialization (serializers.ModelSerializer):
    class Meta:
        model = message
        fields = ['email', 'message']


class UserMessagePostSerialization (serializers.ModelSerializer):
    class Meta:
        model = user_message
        fields = ['message']
