from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.views.decorators.csrf import csrf_exempt

from .models import *
# from .forms import *
from .models import *
from events.models import Event
from employees.models import Employee
import json
from locations.models import LocationCategory

def company_profile(request):
    roles = CompanyProfileRole.objects.all()
    context = {'obj':'Profile', 'roles':roles}
    return render(request, 'company_profile/company_profile.html', context)

@csrf_exempt
def company_roles(request):
    if request.method == 'POST':
        saved_roles = CompanyProfileRole.objects.all()
        roles = json.loads(request.POST.get('roles'))
        l = []
        for verbose_name, short_name in roles['roles'].items():
            l.append(verbose_name)
            try:
                obj = CompanyProfileRole.objects.get(verbose_name__exact=verbose_name)
            except:
                obj = False
            if obj:
                flag = (obj.short_name == short_name)
                if not flag:
                    obj.short_name = short_name
                    obj.save()
            else:
                obj = CompanyProfileRole()
                obj.verbose_name = verbose_name
                obj.short_name = short_name
                obj.save()
        
        for role in saved_roles:
            verbose_name = role.verbose_name
            if verbose_name not in l:
                obj = CompanyProfileRole.objects.get(verbose_name__exact=verbose_name)
                obj.delete()
    return HttpResponse('Hello, world!')