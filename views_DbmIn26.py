from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import generics
from chat.models import(
    Message,
)
from chat.serializers import(
    UserSerializer,
    MessageSerializer,
    RegisterSerializer,
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db.models import Q


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        serializer.save(sender= self.request.user)
        #message = Message.objects.filter(Q(user =self.request.user) & Q(is_active = True))
        #message = message.update(is_active = False)
    
   
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(sender=request.user)
        print("eeeeeeeeeeeeeeeeeeeee", queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
        #cart_obj.update(is_active = False)
        #cart_obj =Cart.objects.filter(Q(user = self.request.user) & Q(is_active = True))
