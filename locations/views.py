from django.shortcuts import render
from django.http import HttpResponse
from django.forms import inlineformset_factory

from .forms import *
from .models import *
from events.models import Event
from employees.models import Employee

def location_list_view(request):
    if request.method == "POST":
        location_form = LocationForm(request.POST)
        if location_form.is_valid():
            created_location = location_form.save(commit=False)
            formset = PositionFormSet(request.POST, instance=created_location)
            if formset.is_valid():
                formset.save()
                created_location.save()

    form = LocationForm()
    context = {
        'employees':Employee.objects.all(),
        'events':Event.objects.all(),
        'locations':Location.objects.all().order_by('location_id'),
        'form':form,
        'obj':'location',
    }
    return render(request, './objects/object_list.html', context)