from django.contrib import admin
from .models import Event, Schedule

# class ScheduleAdmin(admin.ModelAdmin):
#     list_display = ('schedule_name',)

class PositionInline(admin.StackedInline):
    model = Schedule
    fields = (('event', 'employees','locations'),)

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title","doors_open")}
    list_display = ('event_id','title','doors_open','slug', 'alcohol',)
    inlines = [PositionInline]

admin.site.register(Event, EventAdmin)
# admin.site.register(Schedule, ScheduleAdmin)



# class PositionInline(admin.StackedInline):
#     model = Position
#     fields = (('position', 'code'),)

# class LocationAdmin(admin.ModelAdmin):
#     list_display = ('title', 'location_id','bar',)
#     fields = (('title','location_id','bar'),)
#     inlines = [PositionInline]

# admin.site.register(Location, LocationAdmin)