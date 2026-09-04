from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Subject(models.Model):
    title = models.CharField("Назва предмета", max_length=100)

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предмети"

    def __str__(self):
        return self.title

class Grade(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='grades',
        verbose_name="Учень"
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name='grades',
        verbose_name="Предмет"
    )
    value = models.PositiveSmallIntegerField("Оцінка")
    date = models.DateField("Дата", auto_now_add=True)
    comment = models.CharField("Тема / Коментар", max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Оцінка"
        verbose_name_plural = "Оцінки"
        ordering = ['-date']

    def __str__(self):
        return f"{self.student.get_full_name() or self.student.username} — {self.subject.title}: {self.value}"