from django.shortcuts import render
from rest_framework import views,viewsets
from apps.uber.models import Driver
from apps.uber.serializers import DriverSerializer


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


