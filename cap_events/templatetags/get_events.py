from django import template

register = template.Library()

from cap_events.models import Event

import datetime

@register.assignment_tag
def get_all_events():
    events = Event.objects.all()
    return events


@register.assignment_tag
def get_events():
    events = Event.objects.filter(date__gte=datetime.datetime.now())
    return events


