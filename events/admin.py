from django.contrib import admin

from events.models import Event, RSVP

admin.site.register(Event)
admin.site.register(RSVP)
