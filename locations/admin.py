from django.contrib import admin
from .models import Location, Position

class PositionInline(admin.StackedInline):
    model = Position
    fields = ('code','verbose_name','short_name',)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('title', 'location_id','bar','created','modified',)
    fields = (('title','location_id','bar'),)
    inlines = [PositionInline]
    
admin.site.register(Location, LocationAdmin)