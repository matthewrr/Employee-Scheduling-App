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

    context = {
        'obj':'SMS Text',
    }
    return render(request, 'sms/sms_text.html', context)