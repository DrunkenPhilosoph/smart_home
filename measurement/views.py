# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
import json
from datetime import datetime
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer


class Measurements(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    def post(self, request):
        request_data = request.body.decode('utf-8')
        daict_data = json.loads(request_data)
        data = Measurement.objects.create(sensors_id=daict_data['sensors'], temperature=daict_data['temperature'], datetime=datetime.now())
        return Response({'message': 'Информация датчика успешно записана, id:{data.id}'})


class Sensors(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    def post(self, request):
        request_data = request.body.decode('utf-8')
        data = Sensor.objects.create(**json.loads(request_data))
        return Response({'message': f'Датчик успешно добавлен, id:{data.id}'})

    def patch(self, request, pk):
        # request_data = request.body.decode('utf-8')
        instance = Sensor.objects.get(pk=pk)
        serializer = SensorDetailSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        print(serializer)
        return Response({'message': f'Датчик успешно обновлен, id:{pk}'})


class SensorCreate(CreateAPIView):
    serializer_class = SensorDetailSerializer
    # def get(self, request):
    #     sensor = Sensor.objects.all()
    #     serialize_sensor = SensorDetailSerializer(sensor, many=True)
    #     return Response(serialize_sensor.data)
   #  def post(self, request):
   #      request_data = request.body.decode('utf-8')
   #      data = Sensor.objects.create(**json.loads(request_data))
   #      return Response({'message': f'Датчик успешно добавлен, id:{data.id}'})
   # # def put(self, request):
   # #     request_data = request.body.decode('utf-8')
   # #     data =Sensor.objects.update(**json.loads(request_data))
