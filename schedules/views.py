from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
def schedule_list(request):
    return HttpResponse('Hello, world!')