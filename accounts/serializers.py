from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

    validate_password = make_password
