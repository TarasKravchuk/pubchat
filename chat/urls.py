from django.urls import path
from .views import Messages, UserMessages, SingleMessage, SingleUserMessage

urlpatterns = [
  path('list/<int:page>/', Messages.as_view()),
  path('single/<int:id>/', SingleMessage.as_view()),
  path('user/single/<int:id>/', SingleUserMessage.as_view()),
  path('user/list/<int:page>/', UserMessages.as_view()),
]
