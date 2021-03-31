from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'isAdmin',
        )

    def get_isAdmin(self, user):
        return user.is_staff

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = User
        fields = (
            'token',
            'id',
            'first_name',
            'last_name',
            'email',
            'isAdmin',
        )
        
    def get_token(self, user):
        token = RefreshToken.for_user(user)
        return str(token.access_token)