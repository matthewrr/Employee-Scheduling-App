from django.contrib import admin
from .models import Location, Position, LocationCategory

class PositionInline(admin.StackedInline):
    model = Position
    fields = ('code','verbose_name','short_name',)

class LocationCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'color',)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location_id','bar','created','modified',)
    fields = (('title','location_id','category','bar'),)
    inlines = [PositionInline]
    
admin.site.register(Location, LocationAdmin)
admin.site.register(LocationCategory, LocationCategoryAdmin)