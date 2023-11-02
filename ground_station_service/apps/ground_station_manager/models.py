from django.db import models
from django.core.exceptions import ValidationError

import logging

logger = logging.getLogger(__name__)

class GroundStation(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return self.name

    # Override the save method to check if there is already an active GroundStation
    def save(self, *args, **kwargs):
        if self.status == 'active':
            # Query to check if any other active GroundStation exists
            logger.info("Checking if there is already an active GroundStation")    
            existing_active_station = GroundStation.objects.filter(status='active').exclude(pk=self.pk)
            if existing_active_station.exists():
                logger.error(f"Another Active GroundStation: {existing_active_station.first().name} already exists.")
                raise ValidationError("Another active GroundStation already exists.")
        
        
        elif self.status == 'inactive':
            logger.info("Checking if there is already an active GroundStation")    
            existing_active_station = GroundStation.objects.filter(status='active').exclude(pk=self.pk)
            if not existing_active_station.exists():
                logger.error(f"Cannot set {self.name} to inactive as no other active GroundStation exists.")
                raise ValidationError("There is no active GroundStation.")
        
        super(GroundStation, self).save(*args, **kwargs)