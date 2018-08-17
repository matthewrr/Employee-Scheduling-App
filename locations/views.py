import csv
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string

from .forms import LocationForm
from .models import *
from company_profile.models import CompanyProfileRole
import json

from django.views.decorators.csrf import csrf_exempt


    

def location_list(request):
    locations = Location.objects.all().order_by('location_id')
    return render(request, 'objects/list.html', {'locations': locations, 'obj':'location', 'objs':'locations'})

def location_create(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
    else:
        form = LocationForm()
    return save_location_form(request, form, 'objects/create.html')

@csrf_exempt
def positions_create(request):
    pass
    if request.method == 'POST':
        positions = request.POST.get('positions')
        positions = json.loads(positions)
        location_id = request.POST.get('location')
        location = get_object_or_404(Location, location_id=location_id)
        # location = json.loads(location)
        for short_name, verbose_name in positions.items():
            position = location.position_set.create(position=verbose_name, code=short_name)
        
            
            
            # position = Position()
            # position.location = 
            # position.position = verbose_name
            # position.code = short_name
            # position.save()
        
        
        # new_article = r.article_set.create(headline="John's second story", pub_date=date(2005, 7, 29))
        # schedule = get_object_or_404(Schedule, pk=pk) if pk else Schedule()
        
        
        
        
        return HttpResponse('Hello')

def save_location_form(request, form, template_name):
    data = dict()
    roles = CompanyProfileRole.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            locations = Location.objects.all().order_by('location_id')
            data['html_object_list'] = render_to_string('locations/location_list_ajax.html', {
                'locations': locations,
            })
        else:
            data['form_is_valid'] = False
        
    context = {'form': form, 'obj':'location', 'roles':roles}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def location_update(request, pk):
    location = get_object_or_404(Location, pk=pk)
    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)
    else:
        form = LocationForm(instance=location)
    return save_location_form(request, form, 'objects/update.html')

def location_delete(request, pk):
    location = get_object_or_404(Location, pk=pk)
    data = dict()
    if request.method == 'POST':
        location.delete()
        data['form_is_valid'] = True
        locations = Location.objects.all().order_by('location_id')
        data['html_object_list'] = render_to_string('locations/location_list_ajax.html', {
            'locations': locations,
        })
    else:
        context = {'object': location, 'obj': 'location',}
        data['html_form'] = render_to_string('objects/delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

def export_locations(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="all_locations.csv"'

    writer = csv.writer(response)
    writer.writerow(['location_id','title','bar'])

    locations = Location.objects.all().values_list('location_id', 'title', 'bar')
    for location in locations:
        writer.writerow(location)

    return response