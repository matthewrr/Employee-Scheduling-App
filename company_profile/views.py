from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse
from django.forms import inlineformset_factory

# from .forms import *
from .models import *
from events.models import Event
from employees.models import Employee

def company_profile(request):

    context = {
        'obj':'Profile',
    }
    return render(request, 'company_profile/company_profile.html', context)