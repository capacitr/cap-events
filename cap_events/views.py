# Create your views here.
from django.shortcuts import render, get_object_or_404

import models

def get_event(req, slug):
    event = get_object_or_404(models.Event, slug=slug)
    return render(req, 'event.html', {'event' : event})


