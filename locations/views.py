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
    #make sure to delete
    if request.method == 'GET':
        location_id = request.GET.get('location')
        print('location_id is: ' + location_id)
        location = get_object_or_404(Location, location_id=location_id)
        p_set = location.position_set.all()
        
        positions = {}

        for p in p_set:
            positions[p.code] = p.position
        print(positions)
        return HttpResponse(json.dumps(positions))
        
        
        
    if request.method == 'POST':
        
        
        positions = request.POST.get('positions')
        positions = json.loads(positions)
        location_id = request.POST.get('location')
        location = get_object_or_404(Location, location_id=location_id)
        # location = json.loads(location)
        
        p_set = location.position_set.values('code')
        print('pset is:')
        print(p_set)
        keys = p_set
        
        for k,v in enumerate(p_set):
            print(str(v.values()))
        
        short = []
        
        for short_name, verbose_name in positions.items():
            short.append(short_name)
            if short_name in keys:
                pass
            else:
                location.position_set.create(position=verbose_name, code=short_name)
        
        for key in keys:
            if key not in short:
                position = Position.objects.get(location=location)
                print('deleting')
                print(position)
                position.delete()
                # location.position_set.delete(code=key)
            
        
        return HttpResponse('Hello')

def save_location_form(request, form, template_name):
    data = dict()
    
    # get location positionset
    # position_set = 
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
    # data['position_set'] = position_set
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