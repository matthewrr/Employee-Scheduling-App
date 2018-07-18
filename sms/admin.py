from django.contrib import admin

from .models import SMS

class SMSAdmin(admin.ModelAdmin):
    list_display = ('command', 'response',)
    # fields = (('title','location_id','bar'),)
    # inlines = [PositionInline]

admin.site.register(SMS, SMSAdmin)
