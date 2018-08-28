from django.db import models
from django.utils import timezone
from jsonfield import JSONField

class CompanyProfile(models.Model):
    company_name = models.CharField(max_length=256)
    # roles = JSONField(blank=True,null=True)
    # company_logo = pass
    # fk admin users
    created      = models.DateTimeField(editable=False,null=True)
    modified     = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(CompanyProfile, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class CompanyProfileRole(models.Model):
    verbose_name = models.CharField(max_length=256,null=True, blank=True)
    short_name = models.CharField(max_length=256,null=True, blank=True)
    color = models.CharField(max_length=256,null=True, blank=True)