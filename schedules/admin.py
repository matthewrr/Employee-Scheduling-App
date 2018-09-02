from django.contrib import admin
from .models import Schedule

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('title','modified','active_locations','scheduled','shifts','template',)

admin.site.register(Schedule, ScheduleAdmin)