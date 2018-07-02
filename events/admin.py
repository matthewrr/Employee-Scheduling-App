from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_id','title','doors_open')

# Register your models here.
admin.site.register(Event, EventAdmin)