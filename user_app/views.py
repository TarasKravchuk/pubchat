from rest_framework import permissions
from user_app.validator import email_valid
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializator import *
# Create your views here.


class UserRegistrstion (APIView):
    permission_classes = [permissions.AllowAny,]
    def get (self, request):
        return Response(status=201)

    def post (self, request):

        try:
            user = User.objects.create(
                username=request.data['username'],
                first_name=request.data['first_name'],
                last_name=request.data['last_name'],
            )
            user.set_password(request.data['password'])
            email = request.data['email']
            if email_valid(email) is False:
                return Response(status=400)
            chat_user = ChatUser.objects.create(
                user_email=request.data['email'],
                user=user
            )
            chat_user.save()
            return Response(status=201)
        except:
            return Response(status=400)



