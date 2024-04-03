from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Measurement(models.Model):
    sensors = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField()
