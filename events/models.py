from django.db import models
from django.template.defaultfilters import slugify
from schedules.models import Schedule
from employees.models import Employee
from locations.models import Location, Position
import datetime
    
from django.db import models
from jsonfield import JSONField
    
class Event(models.Model):
    title = models.CharField(max_length=256)
    date = models.DateField(blank=False)
    doors_open = models.CharField(max_length=256, verbose_name="Doors Open")
    alcohol = models.BooleanField(default=True)
    slug = models.SlugField()
    schedule = models.OneToOneField(Schedule, on_delete=models.CASCADE, null=True, blank=True)
    
    @property
    def event_category(self):
        return True if self.date < datetime.date.today() else False

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Event, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title