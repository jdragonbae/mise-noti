from django.db import models


# Create your models here.


class Schedule(models.Model):
    scheTitle = models.TextField()
    location = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    micro_dust = models.CharField(max_length=255, blank=True)
