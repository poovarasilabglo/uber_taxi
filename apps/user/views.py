from django.shortcuts import render
from rest_framework import views,viewsets
from apps.user.models import MyUser
from django.contrib.auth import authenticate
from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework import status
from apps.user.serializers import(
     RegisterSerializer,
     UserSerializer)
from apps.user.utils import get_tokens_for_user
from rest_framework import generics
from rest_framework.permissions import AllowAny


class LoginView(views.APIView):
    def post(self, request):
        a = request.data
        if 'username' not in a or 'password' not in a:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        username = a['username']
        password = a['password']
        user = authenticate(request, username=username, password=password)
        print("dfcSDFdsf fsdfsdf",user)
        if user is not None:
            login(request, user)
            auth_data = get_tokens_for_user(user)
            return Response({**auth_data}, status=status.HTTP_200_OK)
        return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer




