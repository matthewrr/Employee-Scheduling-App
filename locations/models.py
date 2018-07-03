from django.db import models

class Location(models.Model):
    location_id = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    total_positions = models.IntegerField(default=6)
    manager_position = models.BooleanField(default=False)
    prep_position = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title