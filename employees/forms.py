from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'employee_id', 'phone_number','food_permit','alcohol_permit','active','admin']

form = EmployeeForm()