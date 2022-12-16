from django.urls import path,include
from rest_framework.routers import DefaultRouter
from apps.passenger.views import PassengerViewSet

router = DefaultRouter()
router.register(r'pass', PassengerViewSet)

urlpatterns = [
    path('',include(router.urls)),
]