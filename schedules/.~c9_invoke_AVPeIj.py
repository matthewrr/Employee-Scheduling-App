from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from .models import Schedule
from locations.models import Location
from employees.models import Employee
from events.models import Event
from company_profile.models import CompanyProfileRole
import json
from pprint import pprint
from datetime import date

def template_list(request):
    templates = Schedule.objects.filter(template=True)
    context = {
        'templates': templates,
        'obj':'template',
        'objs':'templates',
        'app':'event_templates'
    }
    pprint(templates[0].roster)
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
    shifts = {}
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
                    print(flag)
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
                            arrival_time = p.get('arrival_time')
                            if employee: 
                                
                                schedule[loc_id]['scheduled'] += 1
                                
                            schedule[loc_id]['positions'][position.code] = {
                                'employee': employee,
                                'arrival_time': arrival_time,
                                'verbose_name': position.position
                            }
    if template:
        for loc, value in template['locations'].items():
            for p_code in value['positions']:
                if schedule[loc]['positions'].get(p_code):
                    v = template['locations'][loc]['positions'][p_code]
                    schedule[loc]['positions'][p_code] = v
                    # schedule[loc]['positions'][p_code]['verbose_name'] = 
    return schedule

@csrf_exempt
def generate_template(request):
    if request.method == 'POST':
        data = request.POST.get('template')
        roster = schedule_template(template=json.loads(data),new_template=True)
        template = render_to_string('schedules/template.html', {'roster': roster, 'template': True})
        return HttpResponse(template)

@csrf_exempt
def save_template(request):
    if request.method == 'POST':
        
        
        data = request.POST.get('roster')
        
        template = request.POST.get('template')
        title = request.POST.get('title')
        pk = request.POST.get('event_id', None)
        if not pk: pk = request.POST.get('pk', None)
        
        shifts = {'event': pk, 'employees': {}}
        
        data = json.loads(data)
        data = {'locations': data}
        roster = schedule_template(template=data)
        pprint(roster)
        
        active_locations = 0
        if template == 'false':
            for location, attributes in roster.items():
                location = str(location)
                if attributes['active'] == True:
                    active_locations += 1
                    if attributes['positions']:
                        for position, p_attributes in attributes['positions'].items():
                            employee = p_attributes['employee']
                            if employee:
                                print(p_attributes)
                                employee = p_attributes['employee']
                                shifts['employees'][employee] = {
                                    'location_id':location,
                                    'location': roster[location]['location'],
                                    'verbose_name': p_attributes['verbose_name'],
                                    'short_name':position,
                                    'arrive':p_attributes['arrival_time'],
                                }
        event = ''
        schedule = ''
        if template == 'true':
            schedule = get_object_or_404(Schedule, pk=pk) if pk else Schedule()
            schedule.title = title
            schedule.template = True
            schedule.roster = {'locations': roster}
            for k, v in roster.items():
                if v['active'] == True:
                    active_locations += 1
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
                schedule.shifts = shifts
                schedule.save()
            else:
                schedule = Schedule()
                schedule.roster = roster
                schedule.title = event.title
                schedule.event = event
                schedule.template = False
                schedule.scheduled = total_scheduled
                schedule.active_locations = active_locations
                schedule.shifts = shifts
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
        'schedule':schedule,
        'template':True
    }
    return render(request, 'schedules/create.html', context)

@csrf_exempt
def modal_template(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        if category == 'future-events': options = Event.objects.filter(date__gte=date.today())
        elif category == 'previous-events': options = Event.objects.filter(date__lt=date.today())
        elif category == 'all-templates': options = Schedule.objects.filter(template=True)
        template = render_to_string('event_templates/select_template.html', {'options': options})
        return HttpResponse(template)

@csrf_exempt
def select_template(request):  
    pk = request.POST.get('pk')
    category = request.POST.get('category')
    all_employees = Employee.objects.all()
    if category == 'future-events' or category == 'previous-events':
        event = get_object_or_404(Event, pk=pk)
        schedule = get_object_or_404(Schedule, event=event.pk)
        roster = {'locations': schedule.roster}
    elif category == 'all-templates':
        schedule = get_object_or_404(Schedule, pk=pk)
        roster = schedule.roster
    
    context = {'roster': roster['locations'], 'template': False, 'all_employees': all_employees}
    pprint(context)
    template = render_to_string('schedules/template.html', context)
    return HttpResponse(template)
    
    # /210

def employee_schedule(request, num):
    employee = get_object_or_404(Employee, employee_id=num)
    context = {
        'employee': {
            'name': employee.name(),
            'id': employee.employee_id,
            'phone': employee.phone(),
            'food_permit': employee.food_permit,
            'alcohol_permit': employee.alcohol_permit,
        }, 
        'events': {},
        'scheduled': 0
    }
    schedules = Schedule.objects.filter(template=False).values('shifts').order_by('event__date')
    for schedule in schedules:
        shifts = json.loads(schedule['shifts'])
        if shifts.get('employees'):
            shift = shifts['employees'].get(employee.name())
            if shift:
                pk = shifts['event']
                event = get_object_or_404(Event, pk=pk)
                
                if employee:
                    context['events'][event.title] = {}
                    context['scheduled'] += 1
                    context['events'][event.title]['shift'] = shift
                    context['events'][event.title]['details'] = {
                        'title': event.title,
                        'date': event.date,
                        'doors': event.doors_open,
                    }
            else:
                pk = shifts['event']
                event = get_object_or_404(Event, pk=pk)
                context['events'][event.title] = {}
                context['events'][event.title]['shift'] = shift
                context['events'][event.title]['details'] = {
                    'title': event.title,
                    'date': event.date,
                    'doors': event.doors_open,
                }
    return render(request, 'employees/employee_schedule.html', context)