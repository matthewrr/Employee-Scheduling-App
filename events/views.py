from django.shortcuts import render
from django.http import HttpResponse

from .forms import EventForm
from .models import *

def event_list_view(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
    
    form = EventForm()
    context = {
        'employees':Employee.objects.all().order_by('first_name'),
        'events':Event.objects.all().order_by('-date'),
        'locations':Location.objects.all().order_by('location_id'),
        'form':form,
        'obj':'event',
    }
    return render(request, './objects/object_list.html', context)

def event_detail_view(request,year,month,day,slug):
    event = Event.objects.get(date__year=year, date__month=month, date__day=day,slug=slug)
    employees2 = Employee.objects.all()
    l = []
    beg = "<option value='hello'>"
    end = "</option>"
    
    for employee in employees2:
        l.append(beg + employee.first_name + ' ' + employee.last_name + end)
    employee_values = ('').join(l)
    
    context = {
        'event':event,
        'employees':Employee.objects.all(),
        'locations':Location.objects.all().order_by('location_id'),
        'all_employees': employee_values,
    }
    

    
    return render(request, './events/detail/event_detail.html', context)
