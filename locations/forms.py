from django.forms import ModelForm
from .models import Location, Position
from django.forms import inlineformset_factory

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['location_id', 'title', 'bar',]

class PositionForm(ModelForm):
    class Meta:
        model = Position
        exclude = ()

form = LocationForm()

PositionFormSet = inlineformset_factory(Location, Position,
                                            form=PositionForm, extra=1)