from django.db import models

# Create your models here.
from django.db import models

class Intersection(models.Model):
    name = models.CharField(max_length=100)
    # Add any other relevant fields for an intersection

    def __str__(self):
        return self.name

class TrafficData(models.Model):
    intersection = models.ForeignKey(Intersection, on_delete=models.CASCADE)
    traffic_density = models.IntegerField()
    vehicle_size = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.intersection} - {self.timestamp}"
