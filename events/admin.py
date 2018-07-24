from django.contrib import admin
from .models import Event, Shift

# admin.site.unregister(Schedule)


class ShiftInline(admin.StackedInline):
    model = Shift
    # fields = (('event','location','position','employee','arrival_time'),)
    fields = (('locations','position','employees','start_time'),)

# class ScheduleAdmin(admin.ModelAdmin):
#     def event_name(self, obj):
#         try:
#             return obj.event.title
#         except:
#             return "Unassigned"
#     list_display = ('event_name',)
#     inlines = [ShiftInline]

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title","doors_open")}
    list_display = ('title','doors_open','slug', 'alcohol',)
    inlines = [ShiftInline]

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

