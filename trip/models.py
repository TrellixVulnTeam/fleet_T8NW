from django.db import models

# Create your models here.
class Trip(models.Model):
    start = models.CharField(null = True,max_length=10)
    end = models.CharField(null = True,max_length=10)
    vehicle = models.CharField(null = True,max_length=10)
