from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Event


def is_moderator(user):
    return user.is_staff or user.groups.filter(name="Moderators").exists()


def event_list(request):
    events = Event.objects.all()

    return render(request, "GroupPortal/events.html", {
        "events": events,
        "can_manage": request.user.is_authenticated and is_moderator(request.user),
    })


@login_required
def event_create(request):
    if not is_moderator(request.user):
        return redirect("event_list")

    if request.method == "POST":
        Event.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            date=request.POST.get("date"),
            time=request.POST.get("time"),
        )

        return redirect("event_list")

    return render(request, "GroupPortal/event_form.html")


@login_required
def event_edit(request, event_id):
    if not is_moderator(request.user):
        return redirect("event_list")

    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":
        event.title = request.POST.get("title")
        event.description = request.POST.get("description")
        event.date = request.POST.get("date")
        event.time = request.POST.get("time")
        event.save()

        return redirect("event_list")

    return render(request, "GroupPortal/event_form.html", {
        "event": event
    })


@login_required
def event_delete(request, event_id):
    if not is_moderator(request.user):
        return redirect("event_list")

    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":
        event.delete()
        return redirect("event_list")

    return render(request, "GroupPortal/event_delete.html", {
        "event": event
    })