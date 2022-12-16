from rest_framework import serializers
from apps.uber.models import Driver


class DriverSerializer(serializers.ModelSerializer):
    driver_name = serializers.ReadOnlyField(source='name.username')
    class Meta:
        model = Driver
        fields = ['id','driver_name','bio','image','vehicle','passenger_location','contact_info', 'status']