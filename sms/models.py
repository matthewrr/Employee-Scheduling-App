from django.db import models
from django.utils import timezone

class SMS(models.Model):
    command     = models.CharField(max_length=256)
    response    = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    created     = models.DateTimeField(editable=False,null=True)
    modified    = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(SMS, self).save(*args, **kwargs)