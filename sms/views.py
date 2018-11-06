from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse
from django.forms import inlineformset_factory

# from .forms import *
from .models import *
from events.models import Event
from employees.models import Employee

def sms_text(request):
    
    admins = Employee.objects.filter(admin=True)
    texts = SMS.objects.all()

    context = {
        'obj':'SMS Text',
        'admins': admins,
        'texts': texts,
    }
    return render(request, 'sms/sms-text.html', context)