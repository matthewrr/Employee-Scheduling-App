from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from .models import Schedule
from locations.models import Location
import json
from pprint import pprint

def create_template(request):
    schedule = schedule_template()
    context = {
        'schedule': schedule,
        'roles': ['Managers','Cashiers','Preps','Bartenders'],
        'template': True,
    }
    return render(request, './events/templates/create.html', context)

def schedule_template(schedule={},template={}):
    locations = Location.objects.all()
    for loc in locations:
        active = template.get('locations', False).get(loc.title, False) if template else True
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
        template = render_to_string('events/templates/template.html', {'locations': locations})
        return HttpResponse(template)
    return HttpResponse("Uh oh... this should only be accessed via POST requests.")

@csrf_exempt
def save_template(request):
    
    if request.method == 'POST':
        data = request.POST.get('template')
        title = request.POST.get('template_name')
        pk = request.POST.get('pk')
        schedule = schedule_template(template=json.loads(data))
        
        template = get_object_or_404(Template, pk=pk) if pk else Template()
        template.title = title
        template.roster = {'locations': schedule}
        
        return HttpResponse('Successfully saved template!')

    return HttpResponse("Uh oh... this should only be accessed via POST requests.")