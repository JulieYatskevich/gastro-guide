from rest_framework import serializers
from .models import Restaurant, Reviews


class RestaurantSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Restaurant
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Reviews
        fields = '__all__'
