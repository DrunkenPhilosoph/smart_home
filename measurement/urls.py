from django.urls import path

from measurement.views import MeasurementView

urlpatterns = [
    path('get_sensor/', MeasurementView.as_view(), name='get_sensor')
]
