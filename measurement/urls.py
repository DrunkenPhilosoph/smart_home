from django.urls import path

from measurement.views import Measurements, Sensors

urlpatterns = [
    path('sensors/', Sensors.as_view()),
    path('sensors/<pk>/', Sensors.as_view()),
    path('measurements/', Measurements.as_view()),
    path('measurements/<id>/', Measurements.as_view()),
]
