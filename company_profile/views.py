from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .models import *
from events.models import Event
from employees.models import Employee
import json
from locations.models import LocationCategory

def company_profile(request):
    roles = CompanyProfileRole.objects.all()
    categories = LocationCategory.objects.all()
    context = {'obj':'Profile', 'categories':categories, 'roles':roles}
    return render(request, 'company_profile/company_profile.html', context)

@csrf_exempt
def company_roles(request):
    
    if request.method == 'POST':
        categories = json.loads(request.POST.get('categories'))
        keys = []
        for k, v in categories['categories'].items():
            keys.append(k)
            color = v['color']
            current_objs = CompanyProfileRole.objects.all()
            short_name = v['short_name']
            obj, created = CompanyProfileRole.objects.update_or_create(
                verbose_name__exact=k,
                defaults={
                    'color': color,
                    'short_name': short_name,
                    'verbose_name': k
                }
            )
        for item in current_objs:
            if item.verbose_name not in keys:
                CompanyProfileRole.objects.filter(verbose_name__exact=item.verbose_name).delete()
    return HttpResponse('Hello, world!')

@csrf_exempt
def location_categories(request):
    if request.method == 'POST':
        categories = json.loads(request.POST.get('categories'))
        keys = []
        for k, v in categories['categories'].items():
            keys.append(k)
            color = v['color']
            current_objs = LocationCategory.objects.all()
            obj, created = LocationCategory.objects.update_or_create(
                category_name__exact=k,
                defaults={
                    'category_name': k,
                    'color': color
                }
            )
        for item in current_objs:
            if item.category_name not in keys:
                LocationCategory.objects.filter(category_name__exact=item.category_name).delete()
    return HttpResponse('Hello, world!')