from django.urls import path,include
from rest_framework.routers import DefaultRouter
from apps.passenger.views import PassengerBookingViewSet,DriverBookingViewset

router = DefaultRouter()
router.register(r'pass', PassengerBookingViewSet)
router.register(r'book',DriverBookingViewset)

urlpatterns = [
    path('',include(router.urls)),
]