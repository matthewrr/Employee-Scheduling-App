from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from .models import Schedule
from locations.models import Location
from events.models import Event
from company_profile.models import CompanyProfileRole
import json
from pprint import pprint
from datetime import date

def template_list(request):
    templates = Schedule.objects.all()
    context = {
        'templates': templates,
        'obj':'template',
        'objs':'templates',
        'app':'event_templates'
    }
    return render(request, 'objects/list.html', context)

def template_create(request):
    roster = schedule_template()
    context = {
        'roster': roster,
        'template': True,
        'new': True,
    }
    return render(request, 'schedules/create.html', context)
    
def schedule_template(schedule={},template={},new_template=False):
    locations = Location.objects.all()
    
    for location in locations:
        # active = template.get('locations', {}).get(loc.location_id, False) if template else True
        loc_id = str(location.pk)
        if template:
            l = template['locations'].get(loc_id)
            if l: 
                active = l.get('active', False)
            else:
                active = False
        else:
            active = True
        
        schedule[loc_id] = {
            'active': active,
            'bar': location.bar,
            'location': location.title,
            'scheduled': 0,
            'positions': {}
        }
        if template:
            for position in location.position_set.all():
                if new_template:
                    flag = template['locations'].get(loc_id)
                    if flag:
                        schedule[loc_id]['positions'][position.code] = {
                            'employee': '',
                            'arrival_time': '',
                            'verbose_name': position.position
                        }
                else:
                    if template['locations'].get(loc_id):
                        p = template['locations'][loc_id]['positions'].get(position.code)
                        if p:
                            employee = p.get('employee')
                            if employee: schedule[loc_id]['scheduled'] += 1
                            arrival_time = p.get('arrival_time')
                            schedule[loc_id]['positions'][position.code] = {
                                'employee': employee,
                                'arrival_time': arrival_time,
                                'verbose_name': position.position
                            }
                
    if template:
        for loc, value in template['locations'].items():
            for p_code in value['positions']:
                try:
                    exists = schedule[loc]['positions'][p_code]
                except:
                    v = template['locations'][loc]['positions'][p_code]
                    schedule[loc]['positions'][p_code] = v
                    # schedule[loc]['positions'][p_code]['verbose_name'] = 
    print('schedule:')
    return schedule

@csrf_exempt
def generate_template(request):
    if request.method == 'POST':
        data = request.POST.get('template')
        roster = schedule_template(template=json.loads(data),new_template=True)
        template = render_to_string('schedules/template.html', {'roster': roster})
        return HttpResponse(template)

@csrf_exempt
def save_template(request):
    if request.method == 'POST':
        data = request.POST.get('roster')
        template = request.POST.get('template')
        title = request.POST.get('title')
        pk = request.POST.get('pk')
        
        data = json.loads(data)
        data = {'locations': data}
        
        roster = schedule_template(template=data)
        
        active_locations = 0
        for location, attributes in roster.items():
            if attributes['active'] == True:
                active_locations += 1
        
        event = ''
        schedule = ''
        if template == 'true':
            schedule = get_object_or_404(Schedule, pk=pk) if pk else Schedule()
            schedule.title = title
            schedule.template = True
            schedule.roster = {'locations': roster}
            schedule.active_locations = active_locations
            schedule.save()
        else:
            total_scheduled = 0
            
            for location, attributes in roster.items():
                total_scheduled += attributes['scheduled'] 
            pk = request.POST.get('event_id', None)
            event = get_object_or_404(Event, pk=pk)
            try:
                schedule = Schedule.objects.filter(event=event.pk)
            except:
                schedule = ''
            if schedule:
                schedule = Schedule.objects.get(event=event.pk)
                schedule.roster = roster
                schedule.scheduled = total_scheduled
                schedule.active_locations = active_locations
                schedule.save()
            else:
                schedule = Schedule()
                schedule.roster = roster
                schedule.title = event.title
                schedule.event = event
                schedule.template = False
                schedule.scheduled = total_scheduled
                schedule.active_locations = active_locations
                schedule.save()
    # pprint(schedule.roster)
    return HttpResponse('Successfully saved template!')

    
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
    title = schedule.title
    context = {
        'roster': roster,
        'title': title,
        'new': False,
        'schedule':schedule
    }
    return render(request, 'schedules/create.html', context)

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

@csrf_exempt
def select_template(request):  
    roster = ''
    schedule = ''
    pk = request.POST.get('pk')
    category = request.POST.get('category')
    if category == 'future-events' or category == 'previous-events':
        event = get_object_or_404(Event, pk=pk)
        schedule = Schedule.objects.filter(event=event.pk)
    elif category == 'all-templates':
        schedule = get_object_or_404(Schedule, pk=pk)
        roster = schedule.roster
    roster = roster['locations']
    context = {'roster': roster}
    template = render_to_string('schedules/template.html', context)
    return HttpResponse(template)
    
    # /210