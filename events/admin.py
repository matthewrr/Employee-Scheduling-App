from django.contrib import admin
from .models import Event, Schedule

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('schedule_name',)

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title","doors_open")}
    list_display = ('event_id','title','doors_open','slug', 'alcohol',)

admin.site.register(Event, EventAdmin)
admin.site.register(Schedule, ScheduleAdmin)