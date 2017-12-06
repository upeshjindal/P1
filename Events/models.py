from django.db import models
from datetime import datetime

# Create your models here.
class Event(models.Model):
    eventCreationTime = models.DateTimeField(default=datetime.now, blank=True)
    eventType = models.CharField(max_length=5)

