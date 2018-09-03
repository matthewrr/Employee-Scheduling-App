from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
import datetime
from jsonfield import JSONField

from employees.models import Employee
from locations.models import Location, Position
    
class Event(models.Model):
    title        = models.CharField(max_length=256)
    date         = models.DateField(blank=False)
    event_start  = models.CharField(max_length=256, verbose_name="Event Start")
    doors_open   = models.CharField(max_length=256, verbose_name="Doors Open")
    alcohol      = models.BooleanField(default=True)
    slug         = models.SlugField()
    created      = models.DateTimeField(editable=False,null=True)
    modified     = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Event, self).save(*args, **kwargs)
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Event, self).save(*args, **kwargs)
    
    @property
    def event_category(self):
        return True if self.date < datetime.date.today() else False
    
    def __str__(self):
        return self.title