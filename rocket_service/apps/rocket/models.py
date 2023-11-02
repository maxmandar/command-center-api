from django.db import models
from simple_history.models import HistoricalRecords

class Rocket(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=100, unique=True)
    height = models.FloatField()
    mass = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

class Stage(models.Model):
    rocket = models.ForeignKey(Rocket, related_name='stages', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name + ' - ' + self.rocket.name

    class Meta:
            unique_together = ['rocket', 'name', 'code']  # This makes combination of rocket, name, and code unique


    def __str__(self):
        return self.name
