from django.db import models
from jsonfield import JSONField

class Schedule(models.Model):
    title = models.CharField(max_length=256)
    template = models.BooleanField(default=False)
    roster = JSONField(blank=True,null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title