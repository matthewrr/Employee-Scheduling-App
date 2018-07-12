from django.forms import ModelForm
from .models import Event
from django import forms


class EventForm(ModelForm):
    class Meta:
        model = Event
        
        fields = ['event_id', 'title', 'date', 'doors_open','alcohol','slug',]

form = EventForm()

# >>> from django import forms
# >>> name = forms.TextInput(attrs={'size': 10, 'title': 'Your name'})
# >>> name.render('name', 'A name')

class EventFormEdit(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['event_id', 'title', 'date', 'doors_open','alcohol','slug',]

editForm = EventFormEdit()