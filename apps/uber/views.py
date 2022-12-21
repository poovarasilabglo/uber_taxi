from django.shortcuts import render
from rest_framework import views,viewsets
from apps.uber.models import Driver
from apps.uber.serializers import DriverSerializer
from rest_framework.response import Response


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    def perform_create(self, serializer):
        serializer.save(name= self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(name = self.request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)




