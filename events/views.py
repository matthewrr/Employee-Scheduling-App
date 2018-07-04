from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    context = {
        'employees':Employee.objects.all(),
        'events':Event.objects.all(),
        'locations':Location.objects.all().order_by('location_id'),
    }
    return render(request, './events/event_detail.html', context)