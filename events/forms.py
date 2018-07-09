from django.forms import ModelForm
from .models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['event_id', 'title', 'date', 'doors_open','alcohol','slug',]

form = EventForm()