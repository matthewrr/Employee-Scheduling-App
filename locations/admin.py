from django.contrib import admin
from .models import Location, Position

class PositionInline(admin.StackedInline):
    model = Position
    read_only=['position']

class LocationAdmin(admin.ModelAdmin):
    list_display = ('title', 'location_id',)
    inlines = [PositionInline]

# Register your models here.
admin.site.register(Location, LocationAdmin)