from django.db import models

class CompanyProfile(models.Model):
    company_name = models.CharField(max_length=256)
    # company_logo = pass
    # fk admin users
    
    def __str__(self):
        return self.title