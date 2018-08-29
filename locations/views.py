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
    return save_location_form(request, form, 'objects/create.html', new_obj=True)

@csrf_exempt
def positions_create(request):
    
    if request.method == 'GET':
        location_id = str(request.GET.get('location'))
        try:
            location = Location.objects.get(location_id=location_id)
        except:
            return HttpResponse('hi')
        
        p_set = location.position_set.all()
        positions = {}

        for p in p_set:
            positions[p.short_name] = p.verbose_name
        return HttpResponse(json.dumps(positions))
        
    if request.method == 'POST':
        
        category = request.POST.get('category')
        positions = request.POST.get('positions')
        
        positions = json.loads(positions)
        location_id = request.POST.get('location_id')
        print(location_id)
        location = Location.objects.get(location_id=location_id)
        try:
            location = Location.objects.get(location_id=location_id)
            for short_name, verbose_name in positions.items():
                location.position_set.create(verbose_name=verbose_name, short_name=short_name)
            
            return HttpResponse('Hello')
        except:
            pass
        p_set = list(location.position_set.values('short_name'))
        keys = []
        
        for k,v in enumerate(p_set):
            keys.append(p_set[k]['short_name'])
        short = []
        
        for short_name, verbose_name in positions.items():
            short.append(short_name)
            if short_name not in keys:
                location.position_set.create(verbose_name=verbose_name, short_name=short_name)
        
        for key in keys:
            if key not in short:
                Position.objects.filter(location=location, short_name=key).delete()
        
        LocationCategory.objects.filter(category=category).update(location=location.pk)
        
        return HttpResponse('Hello')

def save_location_form(request, form, template_name, new_obj=False):
    data = {}
    roles = {}
    categories = CompanyProfileRole.objects.all()
    default_roles = CompanyProfileRole.objects.all()
    
    try:
        location_id = form['location_id'].value()
        location = Location.objects.get(location_id=location_id)
        location_roles = location.position_set.all()
        for role in location_roles:
            roles.setdefault(role.code, {})
            roles[role.code][role.short_name] = role.verbose_name
    except:
        pass
    
    
    
    for role in default_roles:
        short_name = role.short_name
        roles.setdefault(short_name, {})
            
            
    if new_obj == True:
        categories = LocationCategory.objects.all()
        
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            locations = Location.objects.all().order_by('location_id')
            data['html_object_list'] = render_to_string('locations/location_list_ajax.html', {
                'locations': locations,
            })
        else:
            data['form_is_valid'] = False
        context = {'form': form, 'obj':'location','roles':roles, 'default_roles': default_roles, 'categories':categories}
        data['html_form'] = render_to_string(template_name, context, request=request)
        return JsonResponse(data)
        
    
    
    
    
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
    
    
    
    
    

    categories = LocationCategory.objects.all()
    context = {'form': form, 'obj':'location', 'roles':roles, 'default_roles': default_roles, 'categories':categories}
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