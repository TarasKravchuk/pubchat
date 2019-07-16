from . import views
from rest_framework.authtoken.views import obtain_auth_token
from .serializator import *
from django.urls import path

urlpatterns = [
    path('registration/', views.UserRegistrstion.as_view()),
    path('authorization/', obtain_auth_token),
]
