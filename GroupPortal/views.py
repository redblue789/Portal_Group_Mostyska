from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Grade


@login_required
def journal_view(request):
    # Отримуємо всі оцінки з оптимізацією запитів select_related
    grades = Grade.objects.select_related('student', 'subject').all()

    context = {
        'grades': grades,
    }
    return render(request, 'journal.html', context)