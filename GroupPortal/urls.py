from django.urls import path
from . import views

urlpatterns = [
    # ... інші шляхi ...
    path('journal/', views.journal_view, name='journal'),
]