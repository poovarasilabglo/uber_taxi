from rest_framework import serializers
from django.contrib.auth.models import User
from chat.models import Message
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  
    class Meta:
        model = User
        fields = ['username', 'email','password']


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,
                                   validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True,
                                     required=True, 
                                     validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    token = serializers.SerializerMethodField('get_user_token')

    class Meta:
        model = User
        fields = ('username', 'password', 'password2',
                  'email', 'first_name', 'last_name', 'token')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }
 
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
 
    def create(self, validated_data):
        user = User.objects.create(
        username=validated_data['username'],
        email=validated_data['email'],
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    def get_user_token(self, obj):
        return Token.objects.get_or_create(user=obj)[0].key


class MessageSerializer(serializers.ModelSerializer):
    #sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    #receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    sender = serializers.CharField(source="sender.username", read_only = True)
    receiver_name = serializers.CharField(source="receiver.username", read_only = True)
    class Meta:
        model = Message
        fields = ['id','sender','receiver_name','receiver','message','is_read','updated_on']
