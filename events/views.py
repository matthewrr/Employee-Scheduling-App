from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
import datetime

from .forms import EventForm
from .models import *

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

def event_list(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'objects/list.html', {'events': events, 'obj':'event', 'objs':'events'})

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
    else:
        form = EventForm()
    return save_event_form(request, form, 'objects/create.html')


def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
    else:
        form = EventForm(instance=event)
    return save_event_form(request, form, 'objects/update.html')

def save_event_form(request, form, template_name):
    data = dict()
    try:
        date = str(form['date'].value())
        format_str = '%Y-%m-%d'
        date_obj = datetime.datetime.strptime(date, format_str)
        expired = date_obj < datetime.datetime.today()
    except:
        expired = False
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            events = Event.objects.all().order_by('-date')
            data['html_event_list'] = render_to_string('events/event_list_ajax.html', {
                'events': events,'expired': expired
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form, 'obj':'event'}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    data = dict()
    expired = event.event_category
    if request.method == 'POST':
        event.delete()
        data['form_is_valid'] = True
        events = Event.objects.all().order_by('-date')
        data['html_event_list'] = render_to_string('events/event_list_ajax.html', {
            'events': events, 'expired': expired,
        })
    else:
        context = {'event': event, 'obj': 'event', 'expired': expired,}
        data['html_form'] = render_to_string('objects/delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)