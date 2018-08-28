from django.contrib import admin
from .models import CompanyProfile, CompanyProfileRole
    
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ('company_name','created','modified',)

class CompanyProfileRolesAdmin(admin.ModelAdmin):
    list_display = ('verbose_name', 'short_name', 'color')

admin.site.register(CompanyProfile, CompanyProfileAdmin)
admin.site.register(CompanyProfileRole, CompanyProfileRolesAdmin)