from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from events.models import Event
from locations.models import Location

def employee_list_view(request):
    context = {
        'employees':Employee.objects.all().order_by('first_name'),
        'events':Event.objects.all(),
        'locations':Location.objects.all().order_by('location_id'),
    }
    return render(request, './employees/employee_list.html', context)