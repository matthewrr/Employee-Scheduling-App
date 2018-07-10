from django.forms import ModelForm
from .models import Event
from django import forms


class EventForm(ModelForm):
    class Meta:
        model = Event
        
        fields = ['event_id', 'title', 'date', 'doors_open','alcohol','slug',]
        slug = forms.TextInput(attrs={'size': 10, 'title': 'Your name'})
        slug.render('name', 'A name')

form = EventForm()

# >>> from django import forms
# >>> name = forms.TextInput(attrs={'size': 10, 'title': 'Your name'})
# >>> name.render('name', 'A name')