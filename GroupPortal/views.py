import calendar
from datetime import date

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Event


def is_moderator(user):
    return user.is_staff or user.groups.filter(name="Moderators").exists()


def event_list(request):
    events = Event.objects.all().order_by("date", "time")

    return render(request, "events.html", {
        "events": events,
        "can_manage": request.user.is_authenticated and is_moderator(request.user),
    })


def event_calendar(request):
    today = date.today()

    try:
        year = int(request.GET.get("year", today.year))
        month = int(request.GET.get("month", today.month))
    except (ValueError, TypeError):
        year = today.year
        month = today.month

    if month < 1:
        month = 12
        year -= 1

    if month > 12:
        month = 1
        year += 1

    cal = calendar.Calendar(firstweekday=0)
    weeks = cal.monthdayscalendar(year, month)

    events = Event.objects.filter(
        date__year=year,
        date__month=month
    ).order_by("time")

    calendar_weeks = []

    for week in weeks:
        calendar_week = []

        for day in week:
            day_events = []

            if day != 0:
                day_events = [
                    event for event in events
                    if event.date.day == day
                ]

            calendar_week.append({
                "day": day,
                "events": day_events,
            })

        calendar_weeks.append(calendar_week)

    months = [
        "",
        "Січень",
        "Лютий",
        "Березень",
        "Квітень",
        "Травень",
        "Червень",
        "Липень",
        "Серпень",
        "Вересень",
        "Жовтень",
        "Листопад",
        "Грудень",
    ]

    return render(request, "calendar.html", {
        "year": year,
        "month": month,
        "month_name": months[month],
        "weeks": calendar_weeks,
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

    return render(request, "event_form.html")


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

    return render(request, "event_form.html", {
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

    return render(request, "event_delete.html", {
        "event": event
    })