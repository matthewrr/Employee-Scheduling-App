from django.forms import ModelForm
from .models import Event
from django import forms

class EventForm(ModelForm):
    class Meta:
        model = Event
        
        fields = ['title', 'date', 'doors_open','alcohol','slug',]

# form = EventForm()

# class EventFormEdit(forms.ModelForm):

#     class Meta:
#         model = Event
#         fields = ['event_id', 'title', 'date', 'doors_open','alcohol','slug',]

# editForm = EventFormEdit()

# class ScheduleForm(forms.ModelForm):
#     class Meta:
#         model = Schedule
#         # exclude = ['author', 'updated', 'created', ]
#         fields = ['text']
#         widgets = {
#             'text': forms.TextInput(attrs={
#                 'id': 'post-text', 
#                 'required': True, 
#                 'placeholder': 'Say something...'
#             }),
#         }