from django.contrib.auth.models import User
from rest_framework import serializers
from itemsApp.models import Item, MiddleMan,Address, Order
from rest_framework_jwt.settings import api_settings


import uuid
import warnings
from calendar import timegm
from datetime import datetime
from rest_framework_jwt.compat import get_username
from rest_framework_jwt.compat import get_username_field


def jwt_payload_handler(user):
    username_field = get_username_field()
    username = get_username(user)

    warnings.warn(
        'The following fields will be removed in the future: '
        '`email` and `user_id`. ',
        DeprecationWarning
    )

    payload = {
        'user_id': user.pk,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'username': username,
        'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
    }
    if hasattr(user, 'email'):
        payload['email'] = user.email
    if isinstance(user.pk, uuid.UUID):
        payload['user_id'] = str(user.pk)

    payload[username_field] = username

    # Include original issued at time for a brand new token,
    # to allow token refresh
    if api_settings.JWT_ALLOW_REFRESH:
        payload['orig_iat'] = timegm(
            datetime.utcnow().utctimetuple()
        )

    if api_settings.JWT_AUDIENCE is not None:
        payload['aud'] = api_settings.JWT_AUDIENCE

    if api_settings.JWT_ISSUER is not None:
        payload['iss'] = api_settings.JWT_ISSUER

    return payload


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        new_user = User(first_name=first_name, last_name=last_name, email=email, username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True, allow_blank=True)

    def validate(self, data):
        my_email = data.get('email')
        my_username = data.get('username')
        my_password = data.get('password')

        try:
            user_obj = User.objects.get(email=my_email)
        except:
            raise serializers.ValidationError("This email does not exist")

        if not user_obj.check_password(my_password):
            raise serializers.ValidationError("Incorrect username/password combination!")

        # jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user_obj)
        token = jwt_encode_handler(payload)

        data["token"] = token
        print(data)
        return data



class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'id',
            'name',
            'category',
            'price',
            'image',
            ]

class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'id',
            'name',
            'description',
            'category',
            'price',
            'image',
            ]

class AddressCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude=["user"]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        exclude=["user"]

class MiddleManSerializer(serializers.ModelSerializer):
    class Meta:
        model=MiddleMan
        fields= '__all__'
