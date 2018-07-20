from django.db import models


# Create your models here.


class Schedule(models.Model):
    summary = models.TextField()
    location = models.CharField(max_length=255)
    timezone = models.CharField(max_length=255)
    micro_dust = models.CharField(max_length=255, blank=True)
