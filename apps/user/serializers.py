from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from apps.user.models import MyUser


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=MyUser.objects.all())])
    password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    is_uber = serializers.BooleanField(default=False)
    is_driver = serializers.BooleanField(default=False)
    is_passenger = serializers.BooleanField(default=False)

    class Meta:
        model = MyUser
        fields = ('username', 'password', 'password2',
         'email','is_uber','is_driver','is_passenger', 'first_name', 'last_name')
        extra_kwargs = {
        'first_name': {'required': True},
        'last_name': {'required': True}
        }
 
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
            {"password": "Password fields didn't match."})
        return attrs
 
    def create(self, validated_data):
        print("********", validate_password)
        user = MyUser.objects.create(
        username=validated_data['username'],
        email=validated_data['email'],
        is_uber = validated_data['is_uber'],
        is_driver = validated_data['is_driver'],
        is_passenger = validated_data['is_passenger'],
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id','username', 'email']




