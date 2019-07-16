from django.contrib import admin
from .models import user_message, message
# Register your models here.

admin.site.register(user_message)
admin.site.register(message)
