from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Entrepreneur(models.Model):
    business_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    lunes = models.CharField(max_length=255, blank=True, null=True)
    martes = models.CharField(max_length=255, blank=True, null=True)
    miercoles = models.CharField(max_length=255, blank=True, null=True)
    jueves = models.CharField(max_length=255, blank=True, null=True)
    viernes = models.CharField(max_length=255, blank=True, null=True)
    contact_info = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)

def __str__(self):
    return self.business_name