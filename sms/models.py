from django.db import models

class SMS(models.Model):
    command = models.CharField(max_length=256)
    response = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    # if employee schedule, how many events?
    # profiles/numbers with access
    # who receives response: employees, mgmt, all