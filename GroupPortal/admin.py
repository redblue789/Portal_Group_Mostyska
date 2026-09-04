from django.contrib import admin
from .models import Subject, Grade

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'value', 'date', 'comment')
    list_filter = ('subject', 'date', 'student')
    search_fields = ('student__username', 'student__first_name', 'student__last_name', 'subject__title')
    list_editable = ('value',)  # Дозволяє швидко змінювати оцінки прямо у списку