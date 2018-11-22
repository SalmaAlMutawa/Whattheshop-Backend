from django.contrib.auth.models import User
from rest_framework import serializers
from itemsApp.models import Item


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data

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