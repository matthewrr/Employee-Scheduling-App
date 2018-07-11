from django.db import models
from django.template.defaultfilters import slugify
from employees.models import Employee
from locations.models import Location
import datetime

class Event(models.Model):
    event_id = models.IntegerField(blank=True)
    title = models.CharField(max_length=256)
    date = models.DateField(blank=False)
    doors_open = models.CharField(max_length=256)
    alcohol = models.BooleanField(default=True)
    locations = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    employees = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField()
    
    def expired(self):
        return True if self.date < datetime.date.today() else False
    
    def get_absolute_url(self):
        return ('blog_post_detail', None, {'slug' :self.slug,})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Event, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title