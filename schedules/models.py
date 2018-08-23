from django.db import models
from django.utils import timezone
from jsonfield import JSONField
from events.models import Event

class Schedule(models.Model):
    title        = models.CharField(max_length=256)
    template     = models.BooleanField(default=False)
    roster       = JSONField(blank=True,null=True)
    event        = models.OneToOneField(Event, on_delete=models.CASCADE,null=True,blank=True)
    scheduled    = models.IntegerField(null=True,blank=True)
    created      = models.DateTimeField(editable=False,null=True)
    modified     = models.DateTimeField(null=True)
    active_locations = models.IntegerField(null=True,blank=True)
    shifts =           JSONField(blank=True,null=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Schedule, self).save(*args, **kwargs)
    
    # def name_schedule(self):
    #     if not self.title:
    #         self.title = event.title
    
    def __str__(self):
        return self.title

# event, date, etc.
# employee --> location (short) -->
#                                     +location long
#                                     +pos short
#                                     +pos long
#                                     +arrive