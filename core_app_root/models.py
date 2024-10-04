from django.db import models
from django.conf import settings
# Create your models here.
class CompanyFilesDetails(models.Model):
    logo_file=models.ImageField(height_field=278, width_field=278, max_length=1000)

    def __str__(self):
        return self.logo_file