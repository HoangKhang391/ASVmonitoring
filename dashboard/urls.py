from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('mapSelection/', views.mapSelection, name='dashboard-mapSelection'),
    path('monitoring/', views.monitoring, name='dashboard-monitoring'),
    path('information/', views.info, name='dashboard-info'),
    path('contact/', views.contact, name='dashboard-contact'),
    path('api/get_location_data/', views.get_location_data,
         name='get_location_data'),
    path('api/data-from-asv/', views.SensorDataCreateAPIView.as_view(),
         name='sensor-data-create'),
    path('get_latest_location/', views.get_latest_location,
         name='get_latest_location'),
    path('get_latest_sensor_data/', views.get_latest_sensor_data,
         name='get_latest_sensor_data'),
    path('get_zone_data/', views.get_zone_data, name='get_zone_data'),
    path('api/get_points/', views.get_points, name='get_points'),

]
