from django.urls import path
from . import views

urlpatterns = [
    path("", views.event_list, name="event_list"),
    path("create/", views.event_create, name="event_create"),
    path("rsvp/<int:event_id>", views.event_rsvp, name="event_rsvp")

]