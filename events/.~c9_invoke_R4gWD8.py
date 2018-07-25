import csv, datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.views import View
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .forms import EventForm
from .models import *
from pprint import pprint

#dont fetch is not changed

def event_detail_view(request,year,month,day,slug):
    event = Event.objects.get(slug=slug)
    locations = event.eventschedule.eventlocation_set.all()
    all_employees = Employee.objects.all()
    schedule = {}
    
    #create schedule
    # for location in locations:
    #     schedule[location] = {}
    #     for shift in location.shift_set.all():
    #         schedule[location][shift.position] = {'employee':str(shift.employee),
    #                                               'arrival_time':shift.arrival_time}
    # context = {
    #     'event':event,
    #     'schedule':schedule,
    #     'all_employees': all_employees,
    # }
        

    # if not event.eventschedule:
    context = {
        'event':event,
        'locations':Location.objects.all(),
        'all_employees': Employee.objects.all(),
    }
    
    return render(request, './events/detail/event_detail.html', context)
    
    
    # concerts = Event.objects.all()
    #     @property
    # def location_positions(self):
    #     return self.event
    # schedules = Schedule.objects.all()
    # for c in concerts:
    #     print(c.locations_set.all())
    #     print('bye')
    # print('hello')
    # for schedule in schedules:
    #     print(schedule.event)
    #     print(schedule.locations)
    
    
    # event = Event.objects.get(date__year=year, date__month=month, date__day=day,slug=slug)
    # schedule = Schedule.objects.get(events=event)
    # print(schedule)
    
    # event = Event.objects.get(date__year=year, date__month=month, date__day=day,slug=slug)
    # print(Shift.objects.get())

    
    
    # for c in concerts:
    #     print(c.__dict__)
    #     print(c.schedule_id)
    
    # for s in Schedule.objects.all():
    #     print(s) #name of schedule
    #     # print(s.locations.all()) #active locations
    #     for t in s.locations.all():
    #         print(t)
    #         print(t.position_set.all())
        
    

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
        
    