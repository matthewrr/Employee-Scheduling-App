from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','phone','food_permit','alcohol_permit','admin','active')

# # Register your models here.
admin.site.register(Employee, EmployeeAdmin)