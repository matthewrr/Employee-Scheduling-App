from django.db import models

class Location(models.Model):
    location_id = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    
    def __str__(self):
        return self.title