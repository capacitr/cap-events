from django import template

register = template.Library()

from events.models import Event

@register.assignment_tag
def get_events(tag_name=None):
    events = Event.objects.all()
    return events


