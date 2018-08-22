from django.db import models
from jsonfield import JSONField
from events.models import Event
from django.utils import timezone

class Schedule(models.Model):
    title        = models.CharField(max_length=256)
    template     = models.BooleanField(default=False)
    roster       = JSONField(blank=True,null=True)
    event        = models.OneToOneField(Event, on_delete=models.CASCADE,null=True,blank=True)
    scheduled    = models.IntegerField(null=True,blank=True)
    created      = models.DateTimeField(editable=False)
    modified     = models.DateTimeField()

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