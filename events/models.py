from django.db import models
from django.template.defaultfilters import slugify
from employees.models import Employee
from locations.models import Location, Position
import datetime
    
class Event(models.Model):
    title = models.CharField(max_length=256)
    date = models.DateField(blank=False)
    doors_open = models.CharField(max_length=256,verbose_name="Doors Open")
    alcohol = models.BooleanField(default=True)
    slug = models.SlugField()
    
    @property
    def event_category(self):
        return True if self.date < datetime.date.today() else False

    def mylocations(self):
        print(self.locations)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Event, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class EventSchedule(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE,null=True, blank=True)
    template = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = 'Schedule'
    def __str__(self):
        return "Schedule for: " + self.event.title
  
class EventLocation(models.Model):
    event_schedule = models.ForeignKey(EventSchedule, on_delete=models.CASCADE,null=True, blank=True)
    locations = models.ForeignKey(Location, on_delete=models.CASCADE,null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Locations'
    def __str__(self):
        return self.locations.title

class Shift(Position):
    event_location = models.ForeignKey(EventLocation, on_delete=models.CASCADE, verbose_name="Event Location")
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE,null=True, blank=True)
    arrival_time = models.CharField(max_length=256,null=True, blank=True)