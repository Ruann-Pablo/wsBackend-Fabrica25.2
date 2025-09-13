from rest_framework import serializers
from .models import User, City, Forecast, FavoriteCity

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'city']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'country']

class ForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forecast
        fields = ['id', 'city', 'date', 'temperature', 'humidity', 'wind_speed']

class FavoriteCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteCity
        fields = ['id', 'user', 'city']