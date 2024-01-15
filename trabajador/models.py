from datetime import datetime, timezone
from django.db import models

# Create your models here.
class Area(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str (self.name)

class Worker(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    area = models.ForeignKey(Area, on_delete=models.CASCADE )

    def __str__(self):
        return str (self.name)

def current_time():
    return timezone.localtime(timezone.now()).strftime('%H:%M:%S')

def current_date():
    return timezone.localtime(timezone.now()).strftime('%d/%m/%Y')
class Movements(models.Model):

    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

    def __str__(self):
        return str (self.time)