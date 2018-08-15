from django.db import models
from jsonfield import JSONField

class Schedule(models.Model):
    title = models.CharField(max_length=256)
    template = models.BooleanField(default=False)
    roster = JSONField(blank=True,null=True)
    # event = models.OneToOneField(Event, on_delete=models.CASCADE,null=True,blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    
    # def name_schedule(self):
    #     if not self.title:
    #         self.title = event.title
    
    def __str__(self):
        return self.title