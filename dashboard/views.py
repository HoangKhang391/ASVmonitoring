from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from decimal import Decimal
from .serializers import ResponseFromWebSerializer, DataFromASVSerializer
from .models import Response_From_Web, Data_From_ASV
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from .models import Response_From_Web
from django.core import serializers
from django.shortcuts import render
from .models import Response_From_Web


def index(request):
    return render(request, 'dashboard/index.html')


def get_latest_location(request):
    latest_location = Data_From_ASV.objects.order_by('-created_at').first()
    data = {
        "humidity": latest_location.humidity,
        "temperature": latest_location.temperature,
        "dissolvedOxygen": latest_location.dissolvedOxygen,
        "airPressure": latest_location.airPressure,
        "latitude": latest_location.latitude,
        "longitude": latest_location.longitude,
        "created_at": latest_location.created_at,
    }
    return JsonResponse(data)


def get_latest_sensor_data(request):
    latest_data = Data_From_ASV.objects.latest('created_at')
    data = {
        'temperature': latest_data.temperature,
        'humidity': latest_data.humidity,
        'dissolved_oxygen': latest_data.dissolvedOxygen,
        'pressure': latest_data.airPressure,
        'latitude': latest_data.latitude,
        'longitude': latest_data.longitude,
    }
    return JsonResponse(data)


def mapSelection(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        Response_From_Web.objects.all().delete()

        for item in data:
            Response_From_Web.objects.create(
                zone=item['zone'],
                latitude=item['latitude'],
                longitude=item['longitude']
            )

        return JsonResponse({'status': 'success'})

    existing_data = Response_From_Web.objects.all()
    existing_data_json = serializers.serialize("json", existing_data)

    return render(request, 'dashboard/mapSelection.html', {'points_json': existing_data_json})


def get_points(request):
    points = list(Response_From_Web.objects.values(
        'latitude', 'longitude', 'zone'))
    return JsonResponse(points, safe=False)


@csrf_exempt
def get_points(request):
    points = list(Response_From_Web.objects.values(
        'latitude', 'longitude', 'zone'))
    return JsonResponse(points, safe=False)


def get_zone_data(request):
    zones = Response_From_Web.objects.all()
    zone_data = serializers.serialize('json', zones)
    return JsonResponse(zone_data, safe=False)


def monitoring(request):
    return render(request, 'dashboard/monitoring.html')


def info(request):
    return render(request, 'dashboard/info.html')


def contact(request):
    return render(request, 'dashboard/contact.html')


def loginForm(request):
    return render(request, 'dashboard/test.html')


@api_view(['GET'])
def get_location_data(request):
    data = Response_From_Web.objects.all()
    serializer = ResponseFromWebSerializer(data, many=True)
    coordinate_pairs = []

    for item in serializer.data:
        coordinate_pairs.append(f"{item['latitude']},{item['longitude']}")

    coordinates_str = "/".join(coordinate_pairs)
    return JsonResponse({'coordinates': coordinates_str}, safe=False)


class SensorDataCreateAPIView(APIView):
    def get(self, request, *args, **kwargs):
        sensor_data = Data_From_ASV.objects.all()
        serializer = DataFromASVSerializer(sensor_data, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        # Use SensorDataSerializer instead of Data_From_ASV
        serializer = DataFromASVSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


TOLERANCE = 0.0001  # Adjust the value according to your needs


def get_data_from_zone(zone_id):
    zone = get_object_or_404(Response_From_Web, pk=zone_id)
    data = Data_From_ASV.objects.filter(
        latitude__range=(float(zone.latitude) - TOLERANCE,
                         float(zone.latitude) + TOLERANCE),
        longitude__range=(float(zone.longitude) - TOLERANCE,
                          float(zone.longitude) + TOLERANCE)
    )
    return data


def display_zone_data(request, zone_id):
    zone = get_object_or_404(Response_From_Web, pk=zone_id)
    data = get_data_from_zone(zone_id)

    if not data:
        try:
            next_zone = Response_From_Web.objects.filter(
                pk__gt=zone_id).order_by('pk').first()
            return redirect('display_zone_data', zone_id=next_zone.pk)
        except (Response_From_Web.DoesNotExist, AttributeError):
            return render(request, 'your_template.html', {'zone': zone, 'data': None})

    return render(request, 'your_template.html', {'zone': zone, 'data': data})
