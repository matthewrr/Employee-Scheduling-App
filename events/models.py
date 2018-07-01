from django.db import models
# from .employees import Employee

class Event(models.Model):
    event_id = models.IntegerField(blank=True)
    title = models.CharField(max_length=256)
    doors_open = models.CharField(max_length=256)
    # employees = models.ForeignKey(Employee, blank=True, null=True)