from django.urls import path
from . import views

urlpatterns = [
    path("events/", views.event_list, name="event_list"),
    path("events/create/", views.event_create, name="event_create"),
    path("events/<int:event_id>/edit/", views.event_edit, name="event_edit"),
    path("events/<int:event_id>/delete/", views.event_delete, name="event_delete"),
]