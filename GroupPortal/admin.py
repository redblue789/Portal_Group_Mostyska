from django.contrib import admin
from .models import ForumTopic, ForumPost

admin.site.register(ForumTopic)
admin.site.register(ForumPost)