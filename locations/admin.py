from django.contrib import admin
from .models import Location

class LocationAdmin(admin.ModelAdmin):
    list_display = ('title', 'location_id', 'total_positions')

# Register your models here.
admin.site.register(Location, LocationAdmin)