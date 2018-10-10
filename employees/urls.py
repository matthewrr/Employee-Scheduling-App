from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.employee_list, name='employees'),
    path('create/', views.employee_create, name='employee_create'),
    path('<int:pk>/update/', views.employee_update, name='employee_update'),
    path('<int:pk>/delete/', views.employee_delete, name='employee_delete'),
    path('export_employees/',views.export_employees, name='export_employees'),
    path('list/', views.fetch_employees, name='fetch_employees'),
]