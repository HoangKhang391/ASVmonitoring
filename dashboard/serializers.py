from .models import Response_From_Web
from rest_framework import serializers
from .models import Response_From_Web, Data_From_ASV


class ResponseFromWebSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response_From_Web
        fields = '__all__'


class DataFromASVSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data_From_ASV
        fields = '__all__'
