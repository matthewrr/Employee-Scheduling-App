from django.db import models
from django.utils import timezone

class LocationCategory(models.Model):
    category_name = models.CharField(max_length=256,null=True, blank=True)
    color = models.CharField(max_length=256,null=True, blank=True)
    
    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name_plural = 'Location Categories'

class Location(models.Model):
    location_id = models.CharField(max_length=256,null=True, blank=True,verbose_name='Location ID')
    category = models.ForeignKey(LocationCategory, on_delete=models.SET_NULL,null=True, blank=True)
    title = models.CharField(max_length=256)
    bar = models.BooleanField(default=False)
    created      = models.DateTimeField(editable=False,null=True)
    modified     = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Location, self).save(*args, **kwargs)
    
    @property
    def positions_length(self):
        return len(self.position_set.all())
    
    class Meta:
        ordering = ['location_id']

    def __str__(self):
        return self.title

class Position(models.Model):
   location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True, blank=True)
   verbose_name = models.CharField(max_length=256)
   short_name = models.CharField(max_length=8)
   code = models.CharField(max_length=8)
   
   def __str__(self):
       return self.verbose_name