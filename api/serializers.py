from django.contrib.auth.models import User
from rest_framework import serializers
from itemsApp.models import Item


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

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user_obj)
        token = jwt_encode_handler(payload)

        data["token"] = token
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
