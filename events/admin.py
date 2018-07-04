from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title","doors_open")}
    list_display = ('event_id','title','doors_open','slug', 'employees', 'locations')

# Register your models here.
admin.site.register(Event, EventAdmin)