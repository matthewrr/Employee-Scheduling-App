from django.contrib import admin
from .models import Event, Shift, EventLocation, EventSchedule, Template
import nested_admin

class TemplateAdmin(admin.ModelAdmin):
    list_display = ('event','alcohol','title','schedule')

class ShiftInline(nested_admin.NestedTabularInline):
    model = Shift
    fields = ('employee','event_location','position', 'arrival_time')

class EventLocationInline(nested_admin.NestedStackedInline):
    model = EventLocation
    fields = ('event_schedule','locations',)
    inlines = [ShiftInline]
    
class EventScheduleInline(nested_admin.NestedTabularInline):
    model = EventSchedule
    fields = ('event',)
    inlines = [EventLocationInline]
    
class EventAdmin(nested_admin.NestedModelAdmin):
    prepopulated_fields = {"slug": ("title","doors_open")}
    list_display = ('title','doors_open','slug', 'alcohol',)
    inlines = [EventScheduleInline]

admin.site.register(Event, EventAdmin)
admin.site.register(Template, TemplateAdmin)