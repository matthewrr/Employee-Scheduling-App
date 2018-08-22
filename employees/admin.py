from django.contrib import admin
from .models import Employee
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class EmployeeAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('name','phone','food_permit','alcohol_permit','admin','active','created','modified',)

# # Register your models here.
admin.site.register(Employee, EmployeeAdmin)