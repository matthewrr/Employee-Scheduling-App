from django.shortcuts import render
from django.http import HttpResponse

from .forms import LocationForm
from .models import *
from events.models import Event
from employees.models import Employee

def location_list_view(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            location.save()
    
    form = LocationForm()
    context = {
        'employees':Employee.objects.all(),
        'events':Event.objects.all(),
        'locations':Location.objects.all().order_by('location_id'),
        'form':form,
    }
    return render(request, './locations/location_list.html', context)