from django.db import models

class Location(models.Model):
    location_id = models.CharField(max_length=256,null=True, blank=True)
    title = models.CharField(max_length=256)
    bar = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['location_id']

    def __str__(self):
        return self.title

class Position(models.Model):
   location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True, blank=True)
   position = models.CharField(max_length=256)
   code = models.CharField(max_length=3)
   
   def __str__(self):
       return self.position
    