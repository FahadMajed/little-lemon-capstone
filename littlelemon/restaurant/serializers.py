from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import serializers

from restaurant.models import MenuItem, Booking


class MenuItemSerializer(serializers.ModelSerializer):
    formatted_price = serializers.SerializerMethodField()

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory', 'formatted_price']

    def get_formatted_price(self, obj):
        return f"${obj.price:.2f}"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
