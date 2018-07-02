from django.db import models
from django.core.validators import RegexValidator

class Employee(models.Model):
    first_name = models.CharField(max_length=64, default='')
    last_name = models.CharField(max_length=64, default='')
    employee_id = models.CharField(max_length=8, default='')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    active = models.BooleanField(default=True)
    food_permit = models.BooleanField(default=False)
    alcohol_permit = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    
    def name(self):
        return self.first_name + ' ' + self.last_name
        
    def phone(self):
        p = self.phone_number
        return '({}) {}-{}'.format(p[:3],p[3:6],p[6:])
        
    def __str__(self):
        return self.employee_id