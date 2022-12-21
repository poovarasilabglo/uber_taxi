from rest_framework import serializers
from apps.passenger.models import Passenger


class PassengerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='name.username',read_only=True)
    class Meta:
        model = Passenger
        fields = ['id','name','driver','image','pickup_location','dropoff_location','passenger_contact','is_accepted']
    


class DriverBookingSerializer(serializers.ModelSerializer):
    passenger_name = serializers.CharField(source='name.username',read_only=True)
    image = serializers.ImageField(read_only = True)
    driver_name =serializers.CharField(source = 'driver.name',read_only = True)
    pickup_location = serializers.CharField(read_only = True)
    dropoff_location = serializers.CharField(read_only = True)
    passenger_contact = serializers.CharField(read_only = True)
    class Meta:
        model = Passenger
        fields = ['id','driver_name','passenger_name','image','pickup_location','dropoff_location','passenger_contact','is_accepted']
        
        