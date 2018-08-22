from django.contrib import admin
from .models import Schedule

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('title','created','modified','active_locations','scheduled','template',)

admin.site.register(Schedule, ScheduleAdmin)