from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    # abilities = {
    #     'skills':Abilities.objects.filter(category='skills'),
    #     'tools':Abilities.objects.filter(category='tools'),
    # }
    # projects = {
    #     'coding':Projects.objects.filter(category='coding'),
    #     'design':Projects.objects.filter(category='design'),
    # }
    context = {
        'employees':Employee.objects.all(),
        'events':Event.objects.all(),
        'locations':Location.objects.all()
        # 'locations':Event.objects.location(),
        # 'employees':Event.objects.employees()
    }
    return render(request, './events/index.html', context)
    