from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import EventForm
from .models import Event, RSVP


@login_required
def event_list(request):
    events = Event.objects.all().order_by("start_time")
    return render(request, "events/event_list.html", {"events": events})


@login_required
def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect("event_list")
    else:
        form = EventForm()
    return render(request, "events/event_form.html", {"form": form})


@login_required
def event_rsvp(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    RSVP.objects.get_or_create(event, user=request.user)
    return redirect("event_list")