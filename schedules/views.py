from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from .models import Schedule
from locations.models import Location
from events.models import Event
import json
from pprint import pprint
from datetime import date


def template_list(request):
    templates = Schedule.objects.all()
    return render(request, 'objects/list.html', {'templates': templates, 'obj':'template', 'objs':'templates', 'app':'event_templates'})

def template_create(request):
    roster = schedule_template()
    context = {
        'roster': roster,
        'roles': ['Managers','Cashiers','Preps','Bartenders'],
        'template': True,
        'new': True,
    }
    return render(request, 'schedules/create.html', context)
    
def schedule_template(schedule={},template={}):
    locations = Location.objects.all()
    for loc in locations:
        # active = template.get('locations', {}).get(loc.location_id, False) if template else True
        
        if template:
            try:
                t = loc.title
                l = template['locations'][str(loc.pk)]
                active = l['active']
                if active:
                    active = True
                else:
                    active = False
                
            except:
                active = False
        else:
            active = True
        
        
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
        item = json.loads(data)
        pprint(item)
        roster = schedule_template(template=json.loads(data))
        pprint(roster)
        template = render_to_string('schedules/template.html', {'roster': roster})
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
        
        data = json.loads(data)
        data = {'locations': data}
        
        roster = schedule_template(template=data)
        
        # all_locations = schedule_template()
        
        
        
        if template == 'true':
            schedule = get_object_or_404(Schedule, pk=pk) if pk else Schedule()
            schedule.title = title
            schedule.template = True
            schedule.roster = {'locations': roster}
            schedule.save()
            #redirect or popup
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

def template_delete(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    data = dict()
    if request.method == 'POST':
        schedule.delete()
        data['form_is_valid'] = True
        templates = Schedule.objects.all()
        data['html_object_list'] = render_to_string('schedules/schedule_list_ajax.html', {
            'templates': templates,
        })
    else:
        context = {'object': schedule, 'obj': 'template',}
        data['html_form'] = render_to_string('objects/delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

def template_update(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    roster = schedule.roster['locations']
    pprint(roster)
    title = schedule.title
    context = {
        'roster': roster,
        'title': title,
        'new': False,
    }
    return render(request, 'schedules/create.html', context)
    # return save_schedule_form(request, form, 'objects/update.html')

@csrf_exempt
def modal_template(request):
    
    if request.method == 'POST':
        category = request.POST.get('category')
        if category == 'future-events':
            options = Event.objects.filter(date__gte=date.today())
        elif category == 'previous-events':
            options = Event.objects.filter(date__lt=date.today())
        elif category == 'all-templates':
            options = Schedule.objects.all()
        
        template = render_to_string('event_templates/select_template.html', {'options': options})
        return HttpResponse(template)
    return HttpResponse('This is not good')

@csrf_exempt
def select_template(request):  

    pk = request.POST.get('pk')
    category = request.POST.get('category')
    if category == 'future-events' or category == 'previous-events':
        event = get_object_or_404(Event, pk=pk)
        roster = json.loads(event.schedule)
    elif category == 'all-templates':
        schedule = get_object_or_404(Schedule, pk=pk)
        roster = json.loads(schedule.schedule)
    context = {'locations': roster}
    template = render_to_string('schedules/template.html', context)
    return HttpResponse(template)