from django.conf.urls import url
from django.urls import path
from . import views

from locations.views import *

from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # url(r'^$', views.schedule_list, name='schedules'), #optional /schedules
    # path('schedules/create/', views.create_schedule, name='create_schedule'),
    
    path('templates/create/', views.create_template, name='create_template'),
    path('templates/create/generate/', views.generate_template, name='generate_template'),
    path('templates/create/save/', views.save_template, name='save_template'), 
]


# schedule_template, generate_template