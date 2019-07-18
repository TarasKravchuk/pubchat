from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import message, user_message
from django.core.paginator import Paginator
from .serializator import MessageSerialization, UserMessageSerialization, MessagePostSerialization, UserMessagePostSerialization
#from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from .validator import message_valid
from user_app.validator import email_valid
from user_app.models import ChatUser
# Create your views here.

class Messages(GenericAPIView):
    permission_classes = [permissions.AllowAny,]

    def get_queryset(self):
        return

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserMessagePostSerialization
        elif self.request.method == 'GET':
            return MessageSerialization
        return Response(status=400)

    def get(self, request, page):
        messages = message.objects.all()
        mess_ser = MessageSerialization(messages, many=True)
        data = mess_ser.data
        paginator = Paginator(data, 10)
        result = paginator.get_page(page)
        return Response(result.object_list)

    def post(self, request, page):
        new_message = MessagePostSerialization(data=request.data)
        if new_message.is_valid():
            mess = request.data['message']
            email = request.data['email']
            if email_valid(email) is False:
                return Response(status=400)
            elif message_valid(mess) is False:
                return Response(status=400)
            new_message.save(email=email, message=request.data['message'])
            return Response(status=201)
        else:
            return Response(status=400)


class UserMessages (GenericAPIView):
    def get_queryset(self):
        return

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [permissions.AllowAny(), ]
            return permission_classes
        if self.request.method == 'POST':
            permission_classes = [permissions.IsAuthenticated(),]
            return permission_classes

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserMessageSerialization
        elif self.request.method == 'POST':
            return UserMessagePostSerialization
        else: Response(status=400)


    def get(self, request, page):
        user_messages = user_message.objects.all()
        user_mess_ser = UserMessageSerialization(user_messages, many=True)
        data = user_mess_ser.data
        paginator = Paginator(data, 10)
        result = paginator.get_page(page)
        return Response(result.object_list)

    def post (self, request, page):
        if request.user.is_authenticated:
            new_message = UserMessagePostSerialization(data=request.data)
            if new_message.is_valid():
                mess = request.data['message']
                user = ChatUser.objects.get(user=request.user)
                print(user.user_email)
                if message_valid(mess) is False:
                    return Response(status=400)
                new_message.save(author=user, email=user.user_email, message=mess)
                return Response(status=201)
            else:
                return Response(status=400)


class SingleMessage(GenericAPIView):
    permission_classes = [permissions.AllowAny,]
    serializer_class = MessageSerialization

    def get (self, request, id):
        try:
            mess = message.objects.get(id=id)
        except:
            return Response(status=404)
        mess_ser = MessageSerialization(mess)
        data = mess_ser.data
        return Response(data)


class SingleUserMessage(GenericAPIView):
    permission_classes = [permissions.AllowAny,]
    serializer_class = UserMessageSerialization

    def get (self, request, id):
        try:
            mess = user_message.objects.get(id=id)
        except:
            return Response(status=404)
        mess_ser = UserMessageSerialization(mess)
        data = mess_ser.data
        return Response(data)
