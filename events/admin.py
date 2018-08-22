from django.contrib import admin
from .models import Event
    
class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title","doors_open")}
    list_display = ('title','doors_open','slug','date','alcohol','created','modified',)

admin.site.register(Event, EventAdmin)