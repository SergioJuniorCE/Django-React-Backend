from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    UserSerializer,
    UserSerializerWithToken,
)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data
        for key, value in serializer.items():
            data[key] = value
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def register_user(request):
    """Registers a user"""
    data = request.data
    try:
        email = User.objects.filter(email=data['email'])
        if email:
            raise Exception('email')
        user = User.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )
        serializer = UserSerializerWithToken(user)
        data = serializer.data
        return Response(data)
    except Exception as e:
        if str(e) == 'email':
            reason = f'User with that email already exists'
        else:
            reason = str(e)
        message = {
            'detail': reason
        }
        return Response(message, status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    """Returns the user information"""
    user = request.user
    serializer = UserSerializer(user)
    data = serializer.data
    return Response(data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    """Updates the user profile"""
    user = request.user
    serializer = UserSerializerWithToken(user)
    data = request.data
    user.first_name = data['first_name']
    user.last_name = data['last_name']
    user.username = data['email']
    user.email = data['email']
    
    if data['password'] != '':
        user.password = make_password(data['password'])
    
    user.save()
    
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    data = serializer.data
    return Response(data)