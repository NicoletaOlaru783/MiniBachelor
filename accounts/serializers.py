from django.contrib.auth.models import User
from rest_framework import permissions, serializers
from django.contrib.auth.hashers import make_password
from .models import Account, MyAccountManager


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        # Check if user is authenticated
        permission_classes = [
            permissions.AllowAny
        ]

    def create(self, validated_data):
        user = Account.objects.create(
            name=validated_data['name'],
            surname=validated_data['surname'],
            email=validated_data['email'],
            role=validated_data['role'],
            school=validated_data['school'],
            programme=validated_data['programme'],
            username=validated_data['username'],
            password=make_password(validated_data['password'])
        )
        return user
