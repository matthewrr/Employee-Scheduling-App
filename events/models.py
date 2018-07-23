from django.db import models
from django.template.defaultfilters import slugify
from employees.models import Employee
from locations.models import Location, Position
import datetime
    
class Event(models.Model):
    event_id = models.IntegerField(blank=True)
    title = models.CharField(max_length=256)
    date = models.DateField(blank=False)
    doors_open = models.CharField(max_length=256)
    alcohol = models.BooleanField(default=True)
    # schedule = models.OneToOneField(
    #     Schedule,
    #     on_delete=models.CASCADE,
    #     blank=True,
    #     null=True,
    # )
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

class Schedule(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    locations = models.ManyToManyField(Location)
    employees = models.ManyToManyField(Employee)
    
    def __str__(self):
        return 'Schedule object for: ' + self.schedule_name