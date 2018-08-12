from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from .models import Schedule
from locations.models import Location
from events.models import Event
import json
from pprint import pprint


def template_list(request):
    templates = Schedule.objects.all()
    return render(request, 'objects/list.html', {'templates': templates, 'obj':'template', 'objs':'templates', 'app':'event_templates'})

def template_create(request):
    schedule = schedule_template()
    context = {
        'schedule': schedule,
        'roles': ['Managers','Cashiers','Preps','Bartenders'],
        'template': True,
    }
    return render(request, 'schedules/create.html', context)
    
def schedule_template(schedule={},template={}):
    locations = Location.objects.all()
    for loc in locations:
        active = template.get('locations', {}).get(loc.title, False) if template else True
        schedule[loc.id] = {
            'active': active,
            'bar': loc.bar,
            'location': loc.title,
            'positions': {}
        }
        for position in loc.position_set.all():
            schedule[loc.id]['positions'][position.code] = {
                'employee': position.position,
                'arrival_time': ''
            }
    return schedule

@csrf_exempt
def generate_template(request):
    if request.method == 'POST':
        data = request.POST.get('template')
        locations = schedule_template(template=json.loads(data))
        template = render_to_string('schedules/template.html', {'locations': locations})
        return HttpResponse(template)
    return HttpResponse("Uh oh... this should only be accessed via POST requests.")

@csrf_exempt
def save_template(request):
    
    if request.method == 'POST':
        data = request.POST.get('roster')
        template = request.POST.get('template')
        title = request.POST.get('title')
        pk = request.POST.get('pk')
        event_id = request.POST.get('event_id')
        roster = schedule_template(template=json.loads(data))
        
        if template == 'true':
            schedule = get_object_or_404(Schedule, pk=pk) if pk else Schedule()
            schedule.title = title
            schedule.template = True
            schedule.roster = {'locations': roster}
            schedule.save()
        else:
            roster = request.POST.get('roster')
            pk = request.POST.get('event_id', None)
            event = get_object_or_404(Event, pk=pk)
            event.schedule = roster
            event.save()
        
        return HttpResponse('Successfully saved template!')

    return HttpResponse("Uh oh... this should only be accessed via POST requests.")
    
def export_templates(request):
    return HttpResponse('Meh')

def template_delete(request):
    return HttpResponse('Meh')

def template_update(request):
    return HttpResponse('Meh')