from rest_framework import serializers
from apps.passenger.models import Passenger


class PassengerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='name.username',read_only=True)
    pickup = serializers.CharField(source='locations.pickup_location')
    dropoff = serializers.CharField(source='locations.dropoff_location')
    class Meta:
        model = Passenger
        fields = ['id','name','image','pickup','dropoff','locations','contact_info']