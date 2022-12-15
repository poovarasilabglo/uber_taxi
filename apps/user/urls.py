from django.urls import path,include
from rest_framework.routers import DefaultRouter
from apps.user.views import LoginView,RegisterUserAPIView
from apps.user.views import UserViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('login/', LoginView.as_view()),
    path('register/',RegisterUserAPIView.as_view()),
]