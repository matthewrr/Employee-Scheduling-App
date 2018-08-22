from django.contrib import admin
from .models import Schedule

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('title','template','created','modified','roster',)

admin.site.register(Schedule, ScheduleAdmin)