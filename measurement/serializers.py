from rest_framework import serializers
from .models import Sensor, Measurement

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'datetime']

class SensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True, read_only=True)
    class Meta:
        model = Sensor
        fields = '__all__'