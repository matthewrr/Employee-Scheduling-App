from django.contrib import admin
from .models import Location, Position

class PositionInline(admin.StackedInline):
    model = Position
    fields = (('position', 'code'),)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('title', 'location_id',)
    fields = (('title','location_id'),)
    inlines = [PositionInline]

admin.site.register(Location, LocationAdmin)