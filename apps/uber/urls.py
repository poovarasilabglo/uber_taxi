from django.urls import path,include
from rest_framework.routers import DefaultRouter
from apps.uber.views import DriverViewSet

router = DefaultRouter()
router.register(r'driver', DriverViewSet)

urlpatterns = [
    path('',include(router.urls)),
]