from django.shortcuts import render
from rest_framework import views,viewsets
from apps.passenger.models import Passenger
from apps.passenger.serializers import PassengerSerializer,DriverBookingSerializer
from rest_framework.response import Response
from apps.user.models import MyUser
from apps.uber.models import Driver
from rest_framework import permissions


class PassengerBookingViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(name= self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(name = self.request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# class DiverOrderViewset(viewsets.ModelViewSet):
#     queryset = DriverOrder.objects.all()
#     serializer_class = DiverOrderSerializer

    # def filter_queryset(self, queryset):
    #     print(queryset.values())
    #     #queryset = queryset.filter(driver = self.request.user.id)
    #     return super().filter_queryset(queryset)


class DriverBookingViewset(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = DriverBookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def filter_queryset(self, queryset):
        print(self.request.user)
        queryset = queryset.filter(driver = Driver.objects.get(name =  self.request.user.id))
        return queryset

    
  

