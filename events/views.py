import csv, datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.views import View
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .forms import EventForm
from .models import *
from pprint import pprint

from django.views.decorators.csrf import csrf_exempt
import json

from django.template.loader import render_to_string


def render_template(request, context):
    return render(request, 'events/templates/template.html', context)
    myhtml = render(request, 'events/templates/template.html', context)
    thing = HttpResponse(myhtml)
    print('printing...')
    print(myhtml)
    print(thing)
    print('done printing.')
    return myhtml
    # return render(request, './events/detail/event_detail.html', context)

@csrf_exempt
def update_schedule(request):
    if request.method == 'POST':
        mydata = request.POST.get('schedule', None)
        pk = request.POST.get('event_id', None)
        event = get_object_or_404(Event, pk=pk)
        event.schedule = mydata
        event.save()
    return HttpResponse("I'm working!")

@csrf_exempt
def generate_template(request):
    # data url in template!
    
    if request.method == 'POST':
    # if request.method == 'GET':
        mydata = request.POST.get('template', None)
        # print(mydata)
        # return mydata
        mydata = request.POST.get('template', None)
        title = request.POST.get('template_name', None)
        # pk = request.POST.get('template_id', None)
        pk = False
        template = ''
        if pk:
            template = get_object_or_404(Template, pk=pk)
            template.schedule = mydata
            template.title = title
            template.save()
        else:
            template = Template()
            template.title = title
            template.schedule = mydata
            template.save()
            # print([a for a in dir(template) if not a.startswith('__')])
        
        template = json.loads(template.schedule)
        mycontext = schedule_template(template=template)
        context = {'locations': mycontext}
        # pprint(newtemplate)
        
        # pprint(context)
        
        
        
        rendered = render_to_string('events/templates/template.html', context)
        return HttpResponse(rendered)
        
        return HttpResponse("<div class='hello'>Hello!!!!</div>")
        return JsonResponse(newtemplate)
     

    return HttpResponse("I'm working!")


#dont fetch if not changed
def schedule_template(schedule={},locations=None,template={}):
    locations = Location.objects.all()
    for location in locations:
       
        schedule[str(location.id)] = {}
        
        if template:
            schedule[str(location.id)]['active'] = True if template['locations'][str(location)] else False
        else:
            schedule[str(location.id)]['active'] = True
        schedule[str(location.id)]['bar'] = location.bar
        schedule[str(location.id)]['location'] = str(location)
        schedule[str(location.id)]['positions'] = {}
        for position in location.position_set.all():
            schedule[str(location.id)]['positions'][position.code] = {'employee':str(position),
                                                                      'arrival_time':''
                                                                          }
    return schedule

def event_detail_view(request,year,month,day,slug):
    all_employees = Employee.objects.all()
    event = Event.objects.get(slug=slug)
    template = json.loads(event.schedule) if event.schedule else schedule_template()
    context = {'event':event,
               'schedule':template,
               'all_employees':all_employees,
               'roles': ['Managers','Cashiers','Preps','Bartenders'],
               'template':False,
               }
    return render(request, './events/detail/event_detail.html', context)

def event_list(request):
    events_list = Event.objects.all().order_by('-date')
    paginator = Paginator(events_list, 20)
    page = request.GET.get('page')
    events = paginator.get_page(page)
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
            data['html_object_list'] = render_to_string('events/event_list_ajax.html', {
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
        data['html_object_list'] = render_to_string('events/event_list_ajax.html', {
            'events': events, 'expired': expired,
        })
    else:
        context = {'object': event, 'obj': 'event', 'expired': expired,}
        print(event)
        data['html_form'] = render_to_string('objects/delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)
    
def export_events(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="all_events.csv"'

    writer = csv.writer(response)
    writer.writerow(['event_id', 'title', 'date', 'doors_open', 'alcohol', 'slug'])

    events = Event.objects.all().values_list('event_id', 'title', 'date', 'doors_open', 'alcohol', 'slug')
    for event in events:
        writer.writerow(event)

    return response

def create_template(request):
    schedule = schedule_template()
    context = {'schedule':schedule,
               'roles': ['Managers','Cashiers','Preps','Bartenders'],
               'template':True,
               'detail':'d-none'
               }
    return render(request, './events/templates/create.html', context)