from rest_framework import serializers
from apps.uber.models import Driver
from apps.passenger.models import Passenger


class DriverSerializer(serializers.ModelSerializer):
    driver_name = serializers.CharField(source='name.username', read_only = True)
    #passenger = serializers.ReadOnlyField()
    #pickup_location = serializers.CharField(source = 'passenger.pickup_location', read_only = True)
    #dropoff_location = serializers.CharField(source = 'passenger.dropoff_location', read_only = True)
    #contact_info = serializers.CharField(source = 'passenger.contact_info')
    class Meta:
        model = Driver
        fields = ['driver_name', 
                  'bio', 
                  'image', 
                  'car_brand',
                  'number_plate',
                  'seat_number',
                  'contact_info']
        #depth = 1