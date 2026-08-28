import re
from django.db import models
from django.contrib.auth.models import User

class Material(models.Model):
    MATERIAL_TYPES = (
        ('file', 'Файл / Документ'),
        ('image', 'Зображення'),
        ('youtube', 'YouTube Відео'),
        ('link', 'Зовнішнє посилання'),
    )

    title = models.CharField(max_length=255, verbose_name="Назва")
    description = models.TextField(blank=True, verbose_name="Опис")
    material_type = models.CharField(max_length=10, choices=MATERIAL_TYPES, verbose_name="Тип матеріалу")
    file = models.FileField(upload_to='materials/files/', blank=True, null=True, verbose_name="Файл")
    image = models.ImageField(upload_to='materials/images/', blank=True, null=True, verbose_name="Зображення")
    external_link = models.URLField(blank=True, null=True, verbose_name="Посилання / YouTube URL")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")

    def get_youtube_embed_url(self):
        """Перетворює стандартне посилання YouTube у форманований embed URL."""
        if self.material_type == 'youtube' and self.external_link:
            regex = r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})'
            match = re.search(regex, self.external_link)
            if match:
                return f"https://www.youtube.com/embed/{match.group(1)}"
        return self.external_link

    def __str__(self):
        return self.title