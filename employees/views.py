import csv
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string

from .forms import EmployeeForm
from .models import *

def employee_list(request):
    employees = Employee.objects.all().order_by('first_name')
    return render(request, 'objects/list.html', {'employees': employees, 'obj':'employee', 'objs':'employees'})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
    else:
        form = EmployeeForm()
    return save_employee_form(request, form, 'objects/create.html')

def save_employee_form(request, form, template_name):
    data = dict()
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            employees = Employee.objects.all().order_by('first_name')
            data['html_object_list'] = render_to_string('employees/employee_list_ajax.html', {
                'employees': employees,
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form, 'obj':'employee'}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
    else:
        form = EmployeeForm(instance=employee)
    return save_employee_form(request, form, 'objects/update.html')

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    data = dict()
    if request.method == 'POST':
        employee.delete()
        data['form_is_valid'] = True
        employees = Employee.objects.all().order_by('first_name')
        data['html_object_list'] = render_to_string('employees/employee_list_ajax.html', {
            'employees': employees,
        })
    else:
        context = {'object': employee, 'obj': 'employee',}
        data['html_form'] = render_to_string('objects/delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

def export_employees(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="all_employees.csv"'

    writer = csv.writer(response)
    writer.writerow(['employee_id', 'first_name', 'last_name', 'phone_number', 'active', 'food_permit', 'alcohol_permit', 'admin'])

    employees = Employee.objects.all().values_list('employee_id', 'first_name', 'last_name', 'phone_number', 'active', 'food_permit', 'alcohol_permit', 'admin')
    for employee in employees:
        writer.writerow(employee)

    return response