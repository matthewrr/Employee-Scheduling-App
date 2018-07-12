from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.contrib import messages

from .forms import EventForm, EventFormEdit
from .models import *

from pprint import pprint


from django.http import JsonResponse
from django.template.loader import render_to_string

@csrf_exempt
def event_list_view(request, pk=None):
    form = EventForm()
    if request.method == "POST" and not pk:
        print('no pk 1')
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
    elif request.method == "POST" and pk:
        print('pk!')
        event = get_object_or_404(Event, pk=pk)
        form = EventFormEdit(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
    
    context = {
        'employees':Employee.objects.all().order_by('first_name'),
        'events':Event.objects.all().order_by('-date'),
        'locations':Location.objects.all().order_by('location_id'),
        'form':form,
        'obj':'event',
    }
    return render(request, './objects/object_list.html', context)

@csrf_exempt
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

@csrf_exempt
def event_edit(request,pk=None):
    form = EventForm()
    event = get_object_or_404(Event, pk=pk)
    pprint(vars(event))
    pprint('------------------------------')
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        pprint(vars(form))
        print('form validity pending...')
        if form.is_valid():
            print('form is valid')
            event = form.save(commit=False)
            event.save()
            print('saved')
        else:
            print('form is not valid')
    else:
        form = EventForm(instance=event)
    
    return HttpResponse(form.as_p())

# id, event_id, title, date, doors_open, alcohol, locations/employees, slug

@csrf_exempt
def save_event_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            events = Event.objects.all()
            data['html_event_list'] = render_to_string('events/includes/partial_event_list.html', {
                'events': events
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@csrf_exempt
def event_update(request,pk=None):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
    else:
        form = EventForm(instance=event)
    return save_event_form(request, form, 'events/includes/partial_event_update.html')