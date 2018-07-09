from django.shortcuts import render
from django.http import HttpResponse

from .forms import EmployeeForm
from .models import *
from events.models import Event
from locations.models import Location

def employee_list_view(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            employee.save()
    
    form = EmployeeForm()
    context = {
        'employees':Employee.objects.all().order_by('first_name'),
        'events':Event.objects.all(),
        'locations':Location.objects.all().order_by('location_id'),
        'form':form,
    }
    return render(request, './employees/employee_list.html', context)