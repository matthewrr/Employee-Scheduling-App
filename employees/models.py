from django.db import models
from django.core.validators import RegexValidator
# from .events import Events

class Employee(models.Model):
    name = models.CharField(max_length=256)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    employee_id = models.IntegerField(blank=True)
    active = models.BooleanField(default=True)
    food_permit = models.BooleanField(default=False)
    alcohol_permit = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)