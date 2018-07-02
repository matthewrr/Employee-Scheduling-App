from django.db import models
from employees.models import Employee
from locations.models import Location

class Event(models.Model):
    event_id = models.IntegerField(blank=True)
    title = models.CharField(max_length=256)
    date = models.DateField(blank=True)
    doors_open = models.CharField(max_length=256)
    locations = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    employees = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.title