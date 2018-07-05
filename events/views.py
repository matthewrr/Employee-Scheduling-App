from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def event_list_view(request):
    context = {
        'employees':Employee.objects.all(),
        'events':Event.objects.all(),
        'locations':Location.objects.all().order_by('location_id'),
    }
    return render(request, './events/event_list.html', context)

def event_detail_view(request,year,month,day,slug):
    event = Event.objects.get(date__year=year, date__month=month, date__day=day,slug=slug)
    context = {
        'event':event,
        'employees':Employee.objects.all(),
        'locations':Location.objects.all().order_by('location_id'),
    }
    return render(request, './events/event_detail.html', context)