from django.db import models
from django.contrib.auth.models import User

class ForumTopic(models.Model):
    title = models.CharField(max_length=200, verbose_name="Тема")
    description = models.TextField(blank=True, verbose_name="Опис")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='forum_topics', verbose_name="Автор")

    def __str__(self):
        return self.title

class ForumPost(models.Model):
    topic = models.ForeignKey(ForumTopic, on_delete=models.CASCADE, related_name='posts', verbose_name="Гілка")
    content = models.TextField(verbose_name="Повідомлення")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='forum_posts', verbose_name="Автор")

    def __str__(self):
        return f"Повідомлення від {self.author.username}"