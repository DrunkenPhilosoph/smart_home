# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response


from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer


class MeasurementView(APIView):
    def get(self, request):
        measurements = Measurement.objects.all()
        serialize_measurements = MeasurementSerializer(measurements, many=True)
        return Response(serialize_measurements.data)

class SensorView(APIView):
    pass