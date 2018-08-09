from django.conf.urls import url
from django.urls import path
from . import views

from locations.views import *

from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.schedule_list, name='schedules'),
    # path('create/', views.location_create, name='location_create'),
]