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

@csrf_exempt
def update_schedule(request):
    if request.method == 'POST':
        mydata = request.POST.get('schedule', None)
        pprint(json.loads(mydata))
        pk = request.POST.get('event_id', None)
        event = get_object_or_404(Event, pk=pk)
        event.schedule = mydata
        event.save()

        ## make sure there's a default schedule (i.e. if not schedule...)
        ## make sure it pull from schedule if available
    
    return HttpResponse("I'm working!")

#dont fetch if not changed
def schedule_template(schedule={},locations=None):
    locations = Location.objects.all()
    for location in locations:
        schedule[str(location)] = {}
        schedule[str(location)]['active'] = True
        schedule[str(location)]['bar'] = location.bar
        schedule[str(location)]['pk'] = location.id
        schedule[str(location)]['positions'] = {}
        for position in location.position_set.all():
            schedule[str(location)]['positions'][position.code] = {'employee':str(position),
                                                 'arrival_time':None
                                                 }
    return schedule

# def schedule_index(request):
#     all_employees = Employee.objects.all()
#     event = Event.objects.get(slug=slug)
#     template = schedule_template()
#     locations = event.eventschedule.eventlocation_set.all()

#     for location in locations:
#         if template.get(str(location)):
#             for position in location.shift_set.all():
#                 template[str(location)]['positions'][str(position)] = {'employee':position.employee,
#                                                                       'arrival_time':position.arrival_time,
#                                                                       }
#     context = {'event':event,
#               'schedule':template,
#               'all_employees':all_employees,
#               'roles': ['Managers','Cashiers','Preps','Bartenders']
#               }
               
#     return render(request, './events/schedule/create.html', context)

# def schedule_create_update(request): #post request
#     #receive dict
#     #dict includes whether template or event
#         # if event, 
#             #check if exists for new or template
#             #connect with one-to-one of template object
#         # else 
#             #check it exists for new or update
#             #create template object without one-to-one
#     return HttpResponse('Hello!')




def event_detail_view(request,year,month,day,slug):
    #simple dicts for location ids employees etc
    # pprint(schedule_template())
    all_employees = Employee.objects.all()
    event = Event.objects.get(slug=slug)
    

    if not event.schedule:
        template = schedule_template()
    else:
        template = json.loads(event.schedule)
        # template = schedule_template()
    pprint(template)
    # locations = event.eventschedule.eventlocation_set.all()
    
    # pprint(template)
    
    myjson = json.loads(event.schedule)


    new_template = True

    # for location in locations:
    #     if template.get(str(location)):
    #         for position in location.shift_set.all():
    #             template[str(location)]['positions'][str(position)] = {'employee':position.employee,
    #                                                                   'arrival_time':position.arrival_time,
    #                                                                   }
    context = {'event':event,
               'schedule':template,
               'all_employees':all_employees,
               'roles': ['Managers','Cashiers','Preps','Bartenders'],
               'new_template':new_template
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

# class ClassView(View):
    
#     def get(self, request):
#         # <view logic>
#         return HttpResponse('result')


# def update_schedule(request):
#     if request.method == 'POST':
#         schedule = request.POST.get('schedule')
#         response_data = {}

        # post = Post(text=post_text, author=request.user)
        # post.save()
        
        # make sure to send pk
        # if event has schedule:
            #replace
        # else
            #create
        
    