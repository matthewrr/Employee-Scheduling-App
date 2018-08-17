from django.forms import ModelForm
from .models import Location, Position

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['location_id', 'title', 'bar',]
form = LocationForm()