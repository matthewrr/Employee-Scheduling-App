from django.db import models
from jsonfield import JSONField

class CompanyProfile(models.Model):
    company_name = models.CharField(max_length=256)
    # roles = JSONField(blank=True,null=True)
    # company_logo = pass
    # fk admin users
    
    def __str__(self):
        return self.title

class CompanyProfileRole(models.Model):
    verbose_name = models.CharField(max_length=256,null=True, blank=True)
    short_name = models.CharField(max_length=256,null=True, blank=True)
    