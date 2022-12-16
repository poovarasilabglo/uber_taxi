from django.shortcuts import render
from rest_framework import views,viewsets
from apps.passenger.models import Passenger
from apps.user.models import MyUser
from apps.passenger.serializers import PassengerSerializer
from rest_framework.response import Response


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    
    def perform_create(self, serializer):
        serializer.save(name= self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(name = self.request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

