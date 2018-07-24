from django.db import models
from django.template.defaultfilters import slugify
from employees.models import Employee
from locations.models import Location, Position
import datetime
    
class Event(models.Model):
    title = models.CharField(max_length=256)
    date = models.DateField(blank=False)
    doors_open = models.CharField(max_length=256)
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

# class Schedule(models.Model):
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)

class Shift(models.Model):
    # schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    locations = models.ForeignKey(Location, on_delete=models.CASCADE,null=True, blank=True)
    position = models.CharField(max_length=256,null=True, blank=True)
    employees = models.ForeignKey(Employee, on_delete=models.CASCADE,null=True, blank=True)
    start_time = models.CharField(max_length=256,null=True, blank=True)