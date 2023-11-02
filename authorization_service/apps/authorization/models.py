from django.db import models
from simple_history.models import HistoricalRecords

class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

class Authorization(models.Model):
    group_name = models.CharField(max_length=100, unique=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    satellite_code = models.CharField(max_length=10)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.group_name
