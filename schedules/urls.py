from django.conf.urls import url
from django.urls import path
from . import views

from locations.views import *

from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # url(r'^$', views.template_list, name='schedules'),
    # path('schedules/create/', views.create_schedule, name='create_schedule'),
    path('employee/<int:num>', views.employee_schedule, name='employee_schedule'),
    url('templates/$', views.template_list, name='templates'),
    path('templates/create/', views.template_create, name='template_create'),
    path('templates/create/generate/', views.generate_template, name='generate_template'),
    path('templates/create/modal/', views.modal_template, name='modal_template'),
    path('templates/create/save/', views.save_template, name='save_template'),
    path('templates/create/select/', views.select_template, name='select_template'),
    path('templates/<int:pk>/delete/', views.template_delete, name='template_delete'),
    path('templates/export/', views.export_templates, name='export_templates'),
    path('templates/<int:pk>/update/', views.template_update, name='template_update'),
]