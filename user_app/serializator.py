from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ChatUser


class BaseUserSerilization (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class UserSerialization (serializers.ModelSerializer):
    user = BaseUserSerilization()
    class Meta:
        model = ChatUser
        fields = ['user', 'user_email']


class BaseUserCreateSerialization(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']
        write_only_fields = ['password']


class ChatUserCreateSerialization(serializers.ModelSerializer):
    user = BaseUserCreateSerialization()
    class Meta:
        model = ChatUser
        fields = ['user', 'user_email']

