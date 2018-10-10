import csv
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template.loader import render_to_string
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.decorators.csrf import csrf_exempt

from .forms import EmployeeForm
from .models import *

@csrf_exempt
def fetch_employees(request):
    return render_to_response('employees/employee_list.json',content_type='application/json')
    return JsonResponse({'first':'Matthew Rivera','second':'Pam McCain','third':'Alisha Rivera'})


def employee_list(request):
    employees_list = Employee.objects.all().order_by('first_name')
    paginator = Paginator(employees_list, 25)
    page = request.GET.get('page')
    employees = paginator.get_page(page)
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