from django.contrib.auth.models import User
from rest_framework import serializers
from itemsApp.models import Item, MiddleMan,Address, Order
from rest_framework_jwt.settings import api_settings


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = __all__

class OrderSerializer(serializers.ModelSerializer):
